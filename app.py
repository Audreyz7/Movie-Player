import os
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")
ALLOWED_EXTENSIONS = {'gif', 'mp4'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
VIDEO_FILE_PATH = ''
filename = ""


def allowed_file(filename): # From Flask Example
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global VIDEO_FILE_PATH
    global filename
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file found")
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            VIDEO_FILE_PATH = filepath
            return redirect(url_for('convert_mp4_to_bmp'))
        
    return render_template('link.html')

@app.route('/convert_bmp', methods=['GET'])
def convert_mp4_to_bmp():
    global VIDEO_FILE_PATH
    
    if not VIDEO_FILE_PATH:
        return "Please upload a video", 400
    
    cap = cv2.VideoCapture(VIDEO_FILE_PATH)
    frame_count = 0
    
    OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs", os.path.splitext(filename)[0])
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    if not cap.isOpened():
        return f"Could not open video: {VIDEO_FILE_PATH}", 400
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        frame_filename = os.path.join(OUTPUT_FOLDER, f"frame_{frame_count:05d}.bmp")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    
    cap.release()
    return f"Converted {frame_count} frames to BMP in {OUTPUT_FOLDER}"

@app.route('/convert_wav', methods=['GET'])
def convert_mp4_to_wav():
    return 

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    