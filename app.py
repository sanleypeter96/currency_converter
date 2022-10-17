import json
import os
import uuid
from flask import Flask, flash, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler

# the "files" directory next to the app.py file
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
#print(UPLOAD_FOLDER)



app = Flask(__name__)
global savedSet
savedSet = set()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'Sick Rat'


def new_file():
    mypath='./files/'
    nameSet=set()
    for file in os.listdir(mypath):
        fullpath=os.path.join(mypath, file)
        if os.path.isfile(fullpath):
            nameSet.add(file)
    retrievedSet=set()
    for name in nameSet:
        stat=os.stat(os.path.join(mypath, name))
        # time=ST_CTIME
        #size=stat.ST_SIZE If you add this, you will be able to detect file size changes as well.
        #Also consider using ST_MTIME to detect last time modified
        retrievedSet.add(name)
    newSet=retrievedSet-savedSet
    deletedSet=savedSet-retrievedSet
    savedSet=newSet


scheduler = BackgroundScheduler()
job = scheduler.add_job(new_file, 'interval', minutes=1)
scheduler.start()

@app.route('/', methods=['GET'])
def main_page():
    return _show_page()

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    #file = request.files['file']
    app.logger.info(request.files)
    upload_files = request.files.getlist('file')
    app.logger.info(upload_files)
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if not upload_files:
        flash('No selected file')
        return redirect(request.url)
    for file in upload_files:
        original_filename = file.filename
        extension = original_filename.rsplit('.', 1)[1].lower()
        filename = str(uuid.uuid1()) + '.' + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_list = os.path.join(UPLOAD_FOLDER, 'files.json')
        files = _get_files()
        files[filename] = original_filename
        with open(file_list, 'w') as fh:
            json.dump(files, fh)

    flash('Upload succeeded')
    return redirect(url_for('upload_file'))

@app.route('/dashboard', methods=['GET'])
def dash():
    #retrive db
    # pass to index.html as arguments
    connection = sqlite3.connect('./database/currency.db')
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute("select * from Currency")
    rows = cur.fetchall();
    return render_template('index.html', rows = rows)



@app.route('/download/<code>', methods=['GET'])
def download(code):
    files = _get_files()
    if code in files:
        path = os.path.join(UPLOAD_FOLDER, code)
        if os.path.exists(path):
            return send_file(path)
    abort(404)

def _show_page():
    files = _get_files()
    return render_template('upload.html', files=files)

def _get_files():
    file_list = os.path.join(UPLOAD_FOLDER, 'files.json')
    if os.path.exists(file_list):
        with open(file_list) as fh:
            return json.load(fh)
    return {}

# if __name__ == "__main__":
#     # Flask hook for cron job
#     scheduler = APScheduler()
#     scheduler.app_job(id = 'check for new files', func = new_file(), trigger = 'interval', seconds = 5)
#     scheduler.start()
#     app.run()