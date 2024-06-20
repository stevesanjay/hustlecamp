from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/audios'

def load_data():
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump({}, f)
    with open('data.json') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'audio_files' not in request.files:
#         return redirect(request.url)

#     files = request.files.getlist('audio_files')
#     data = load_data()
    
#     for file in files:
#         if file.filename == '':
#             continue
        
#         filename = os.path.splitext(file.filename)[0]  # Extract file name without extension
#         file_ext = os.path.splitext(file.filename)[1]  # Extract file extension
#         unique_filename = str(uuid.uuid4()) + file_ext  # Generate unique filename
        
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        
#         audio_id = str(len(data) + 1001)  # Generate new audio_id
#         audio_data = {
#             'original_filename': filename,
#             'audio_location': os.path.join('audios', unique_filename),
#             'ai_feedback': '',  # Placeholder for AI feedback
#             'expert_feedback': ''  # Placeholder for expert feedback
#         }

#         if audio_id in data:
#             data[audio_id].append(audio_data)
#         else:
#             data[audio_id] = [audio_data]

#     save_data(data)
#     return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio_files' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('audio_files')
    data = load_data()
    
    for file in files:
        if file.filename == '':
            continue
        
        filename = os.path.splitext(file.filename)[0]  # Extract file name without extension
        file_ext = os.path.splitext(file.filename)[1]  # Extract file extension
        unique_filename = str(uuid.uuid4()) + file_ext  # Generate unique filename
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        
        audio_id = str(len(data) + 1001)  # Generate new audio_id
        audio_data = {
            ''
            'original_filename': filename,
            'audio_location': os.path.join('audios', unique_filename),
            'ai_feedback': '',  # Placeholder for AI feedback
            'expert_feedback': ''  # Placeholder for expert feedback
        }

        if audio_id in data:
            data[audio_id].append(audio_data)
        else:
            data[audio_id] = [audio_data]

    save_data(data)
    return redirect(url_for('index'))

@app.route('/play/<audio_id>/<index>')
def play_audio(audio_id, index):
    data = load_data()
    audio_data = data.get(audio_id, [])[int(index)]
    return render_template('play.html', audio_data=audio_data)

if __name__ == '__main__':
    app.run(debug=True)
