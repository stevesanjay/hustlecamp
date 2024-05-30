from flask import Flask, render_template, request, redirect, url_for, session
from minio import Minio
from minio.error import S3Error
import os
import json
import urllib.parse

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# MinIO configuration
minio_client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False  # Changed to False to disable HTTPS
)

bucket_name = "fastapi-bucket3"
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)

# JSON file to store audio file locations
AUDIO_LOCATIONS_FILE = 'audio_file_locations.json'

# Ensure the JSON file exists
if not os.path.exists(AUDIO_LOCATIONS_FILE):
    with open(AUDIO_LOCATIONS_FILE, 'w') as f:
        json.dump({}, f)

# To store login attempts
login_attempts = 0
uploaded_files = {}
feedback = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<user_type>', methods=['GET', 'POST'])
def login(user_type):
    global login_attempts
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if user_type == 'candidate' and password == 'candidate':
            session['user'] = username
            session['user_type'] = 'candidate'
            login_attempts += 1
            return redirect(url_for('candidate'))
        elif user_type == 'admin' and username == 'admin' and password == 'admin':
            session['user'] = 'admin'
            session['user_type'] = 'admin'
            return redirect(url_for('admin'))
        else:
            return "Invalid credentials"
    
    return render_template('login.html', user_type=user_type)

@app.route('/candidate', methods=['GET', 'POST'])
def candidate():
    if 'user' not in session or session['user_type'] != 'candidate':
        return redirect(url_for('index'))
    
    message = None
    if request.method == 'POST':
        if 'audio' not in request.files:
            message = "No file part"
        else:
            file = request.files['audio']
            if file.filename == '':
                message = "No selected file"
            if file:
                file_path = f"{session['user']}/{file.filename}"
                try:
                    minio_client.put_object(
                        bucket_name, file_path, file, length=-1, part_size=10*1024*1024
                    )
                    uploaded_files[session['user']] = file_path

                    # Save the file location to JSON
                    with open(AUDIO_LOCATIONS_FILE, 'r+') as f:
                        data = json.load(f)
                        data[f"{session['user']} audio file location"] = file_path
                        f.seek(0)
                        json.dump(data, f, indent=4)

                    message = "File uploaded successfully"
                except S3Error as e:
                    message = f"File upload failed: {e}"
    
    return render_template('candidate.html', message=message)

@app.route('/admin')
def admin():
    if 'user' not in session or session['user_type'] != 'admin':
        return redirect(url_for('index'))
    
    with open(AUDIO_LOCATIONS_FILE, 'r') as f:
        files = json.load(f)
    
    return render_template('admin.html', login_attempts=login_attempts, files=files)

@app.route('/feedback/<filename>', methods=['GET', 'POST'])
def feedback_page(filename):
    if 'user' not in session or session['user_type'] != 'admin':
        return redirect(url_for('index'))
    
    filename = urllib.parse.unquote(filename)  # Decode URL-encoded filename
    if request.method == 'POST':
        feedback[filename] = request.form['feedback']
        return redirect(url_for('admin'))
    
    return render_template('feedback.html', filename=filename)

@app.route('/candidate_feedback')
def candidate_feedback():
    if 'user' not in session or session['user_type'] != 'candidate':
        return redirect(url_for('index'))
    
    user_file = uploaded_files.get(session['user'])
    user_feedback = feedback.get(user_file, "No feedback yet")
    
    return render_template('candidate_feedback.html', feedback=user_feedback)

if __name__ == '__main__':
    app.run(debug=True)