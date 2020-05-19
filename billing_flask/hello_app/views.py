import os
from flask import Flask, redirect, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from . import app
from billing_megafon import billing


# Create a directory in a known location to save files to.
uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)


# Determines the maximum term cache.
@app.after_request
def add_header(response):
    response.cache_control.max_age = 30
    return response


# Checking the downloaded files for allowed extensions.
def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['xlsx', 'html', ])
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Clearing the storage space for the uploaded files.
def clean_uploads(teg):
    file_stor = os.listdir(path=uploads_dir)
    if teg == 'all':
        for file in file_stor:
            os.remove(os.path.join(uploads_dir, file))
    elif teg == 'html':
        extension = set(['html', ])
        for file in file_stor:
            file_name, file_extension = os.path.splitext(file)
            if file_extension[1:].lower() in extension:
                os.remove(os.path.join(uploads_dir, file))


# Downloading files, sending them to check, sending them to the handler.
@app.route('/', methods=['GET', 'POST'])
def upload():
    file_stor = os.listdir(path=uploads_dir)
    # If the file does not match the extension, we catch an error and reload the page.
    try:
        # Checking for extensions and downloading files if they match.
        if request.method == 'POST':
            profile_first = request.files['profile_first']
            profile_second = request.files['profile_second']
            if ((profile_first and allowed_file(profile_first.filename)) and (profile_second and allowed_file(profile_second.filename))):
                profile_first.save(os.path.join(
                    uploads_dir, secure_filename(profile_first.filename)))
                profile_second.save(os.path.join(
                    uploads_dir, secure_filename(profile_second.filename)))
                return redirect(url_for('upload'))
    except TypeError:
        return render_template('upload.html')
    # If two files are uploaded, a handler is started that produces the result.
    if len(file_stor) == 2:
        # Catch errors in file processing (not correct files, files with the same extension, etc.).
        try:
            switch = billing(uploads_dir)
        except:
            clean_uploads('all')
            return render_template('upload.html')
        if switch['switch'] == 0:
            clean_uploads('all')
            return render_template("remarks.html", unknown=switch['unknown'], reserve=switch['reserve'])
        elif switch['switch'] == 1:
            return render_template('finish.html')
    else:
        clean_uploads('all')
        return render_template('upload.html')


# Transfer the finished file to the user.
@app.route('/get_xlsx')
def give_away():
    extension = ['xlsx', ]
    clean_uploads('html')
    file_stor = os.listdir(path=uploads_dir)
    for file in file_stor:
        file_name, file_extension = os.path.splitext(file)
        if file_extension[1:].lower() in extension:
            return send_from_directory(uploads_dir, file, attachment_filename='billing.xlsx', as_attachment=True,)
