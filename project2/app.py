from flask import Flask, render_template, request, redirect, url_for, session
import os
import urllib.parse

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# To store login attempts and uploaded files
login_attempts = 0
uploaded_files = {}
feedback = {}

# Ensure upload folder exists
UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                uploaded_files[session['user']] = file.filename  # Store only the filename
                message = "File uploaded successfully"
    
    return render_template('candidate.html', message=message)

@app.route('/admin')
def admin():
    if 'user' not in session or session['user_type'] != 'admin':
        return redirect(url_for('index'))
    
    return render_template('admin.html', login_attempts=login_attempts, files=uploaded_files)

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