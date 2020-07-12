from flask import request, redirect, Flask, render_template, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename
import os
from PIL import Image


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'

app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['JPEG', 'JPG', 'PNG']
app.config['MAX_IMAGE_FILESIZE'] = 0.5 * 1024 * 1024
exam_list = ['UPSC', 'SSC-CHSL', 'SSC', 'RAILWAYS', 'IBPS', 'IITJEE', 'CLAT', 'CAT', 'XAT']
document_list = ['IDENTITY', 'SIGNATURE']

def allowed_image(filename):

    if not '.' in filename:
        return False

    ext = filename.rsplit('.', 1)[1]

    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config['MAX_IMAGE_FILESIZE']:
        return True
    else:
        return False



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle-upload', methods=['POST'])
def handleFileUpload():
        if request.method == 'POST':

            if request.files:

                if 'filesize' in request.cookies:

                    if not allowed_image_filesize(request.cookies['filesize']):
                        return render_template('index.html', message='File size exceeded maximum limit')

                    photo = request.files['photo']
                    exam_name = request.form['exam']
                    document_name = request.form['document']

                    if photo.filename == '':
                        return render_template('index.html', message='Please check the filename')


                    if allowed_image(photo.filename):

                        filename = secure_filename(photo.filename)

                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                        process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename, exam_name, document_name)

                        return redirect(url_for('uploaded_file', filename=filename))

                    else:
                        return render_template('index.html', message='That file extension is not allowed')


def process_file(path, filename, exam_name, document_name):
    image_resize(path, filename, exam_name, document_name)


def image_resize(path, filename, exam_name, document_name):
    resize_image = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    if exam_name == exam_list[0] and document_name == document_list[0]:
        crop_image = resize_image.resize((140, 110))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
     #sscchsl-image 
    elif exam_name == exam_list[1] and document_name == document_list[0]:
        crop_image = resize_image.resize((110, 120))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #ssc-image
    elif exam_name == exam_list[2] and document_name == document_list[0]:
        crop_image = resize_image.resize((110, 120))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #railway-image
    elif exam_name == exam_list[3] and document_name == document_list[0]:
        crop_image = resize_image.resize((200, 230))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #ibps-image
    elif exam_name == exam_list[4] and document_name == document_list[0]:
        crop_image = resize_image.resize((200, 230))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #iit-image
    elif exam_name == exam_list[5] and document_name == document_list[0]:
        crop_image = resize_image.resize((130, 170))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #clat-image
    elif exam_name == exam_list[6] and document_name == document_list[0]: 
        crop_image = resize_image.resize((200, 230))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #cat-image
    elif exam_name == exam_list[7] and document_name == document_list[0]:
        crop_image = resize_image.resize((110, 170))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #xat-image
    elif exam_name == exam_list[8] and document_name == document_list[0]:
        crop_image = resize_image.resize((200, 230))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #upsc-sign
    elif exam_name == exam_list[0] and document_name == document_list[1]:
        crop_image = resize_image.resize((110, 140))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #sscchsl-sign
    elif exam_name == exam_list[1] and document_name == document_list[1]:
        crop_image = resize_image.resize((140, 60))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #ssc-sign
    elif exam_name == exam_list[2] and document_name == document_list[1]:
        crop_image = resize_image.resize((140, 60))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #railway-sign
    elif exam_name == exam_list[3] and document_name == document_list[1]:
        crop_image = resize_image.resize((140, 60))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #ibps-sign
    elif exam_name == exam_list[4] and document_name == document_list[1]:
        crop_image = resize_image.resize((140, 60))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #iit-sign
    elif exam_name == exam_list[5] and document_name == document_list[1]: 
        crop_image = resize_image.resize((130, 60))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #clat-sign
    elif exam_name == exam_list[6] and document_name == document_list[1]:
        crop_image = resize_image.resize((140, 60))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #cat-sign
    elif exam_name == exam_list[7] and document_name == document_list[1]:
        crop_image = resize_image.resize((300, 132))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    #xat-sign
    elif exam_name == exam_list[8] and document_name == document_list[1]:
        crop_image = resize_image.resize((140, 60))
        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    else:
        return render_template('index.html', message='There is some issue with your file.')


@app.route('/handle-custom-upload', methods=['POST'])
def handlecustomUpload():
        if request.method == 'POST':

            if request.files:

                if 'filesize' in request.cookies:

                    if not allowed_image_filesize(request.cookies['filesize']):
                        return render_template('index.html', message='File size exceeded maximum limit')

                    photo = request.files['photo']
                    image_height = int(request.form['height'])
                    image_width = int(request.form['width'])

                    if photo.filename == '':
                        return render_template('index.html', message='Please check the filename')

                    if allowed_image(photo.filename):

                        filename = secure_filename(photo.filename)

                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                        custom_process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename, image_height, image_width)

                        return redirect(url_for('uploaded_file', filename=filename))
                    else:
                        return render_template('index.html', message='That file extension is not allowed')


def custom_process_file(path, filename, image_height, image_width):
    custom_image_resize(path, filename, image_height, image_width)


def custom_image_resize(path, filename, image_height, image_width):
    custom_resize_image = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    default_image_width, default_image_height = custom_resize_image.size

    if default_image_height > image_height and default_image_width > image_width:

        crop_image = custom_resize_image.resize((image_height, image_width))

        crop_image.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))

    else:

        return render_template('index.html', message='Custom dimensions are bigger than image dimensions!')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)





if __name__ == "__main__":
    app.run()
