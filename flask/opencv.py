from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug import secure_filename
import cv2
import numpy as np


UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'bmp', 'PNG', 'JPG', 'JPEG', 'BMP'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
piccount = np.uint8([0])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            return render_template('binarize.html', filename=filename, originalname=filename)
    return render_template('index.html', filename="test", originalname="test")

@app.route('/binarize', methods=['GET', 'POST'])
def binarize():
    #if request.method == 'POST':
    #    thresh = request.form['thresh']
    #    filename = request.form['filename']
    #    originalname = request.form['originalname']
    #    img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], originalname), 0)
    #    ret, threshImg = cv2.threshold(img, float(thresh), 255, cv2.THRESH_BINARY)
    #    savename = str(piccount[0])+'.bmp'
    #    piccount[0] += 1
    #    cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], savename), threshImg)
    #    return render_template('index.html', filename=savename , originalname=originalname)
    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
