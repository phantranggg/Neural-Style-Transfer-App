#!/usr/bin/env python3

import os
from flask import Flask, render_template, request, Response
import model
import time

app = Flask(__name__)

SRC_FOLDER = os.getcwd() + '/src/'
UPLOAD_FOLDER = os.getcwd() + '/src/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    content = request.files['content_img']
    cf = os.path.join(app.config['UPLOAD_FOLDER'], str(time.time()) + '_' + content.filename)
    content.save(cf)
    content.close()

    isUploadStyle = request.form.get('is_upload_style')
    if isUploadStyle == 'true':
        style = request.files['style_img']
        sf = os.path.join(app.config['UPLOAD_FOLDER'], str(time.time()) + '_' + style.filename)
        style.save(sf)
        style.close()
    else:
        sf = SRC_FOLDER + request.form.get('style')

    model.initSession()
    rs = model.run_model(cf, sf)

    return Response(
        rs,
        mimetype="text/plain",
    )

if __name__ == '__main__':
    app.run(host='localhost', port=8001)