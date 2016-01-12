from flask import Flask, render_template, request, redirect, url_for, make_response
import os
from werkzeug import secure_filename
import cv2
import numpy as np
import io


UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif', 'bmp'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
piccount = np.uint8([0])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def binarize():
        thresh = request.form['thresh']
        img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], 'lenna.png'), 0)
        ret, threshImg = cv2.threshold(img, float(thresh), 255, cv2.THRESH_BINARY)
        result,buf=cv2.imencode('.bmp', threshImg)
        print(buf.size)
        return buf.tostring()

if __name__ == '__main__':
    app.debug = True
    app.run()
