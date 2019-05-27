#!/usr/bin/env python3

import os
from flask import Flask, render_template, request, Response
import model
import time
from PIL import Image

app = Flask(__name__)

SRC_FOLDER = os.getcwd() + '/src/'
UPLOAD_FOLDER = os.getcwd() + '/src/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
WIDTH = 300
HEIGHT = 300

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    content = request.files['content_img']
    cf = os.path.join(app.config['UPLOAD_FOLDER'], str(time.time()) + '_' + content.filename)
    content.save(cf)
    content.close()
    
    if cf[-3:] == 'png':
        im = Image.open(cf)
        rgb_im = im.convert('RGB')
        cf = cf[:-3] + 'jpg'
        rgb_im.save(cf)
        
    content_img = Image.open(cf)
    (content_w, content_h) = content_img.size
    if content_h >= content_w and content_h >= 300:
        content_w = (int)((content_w * 300) / content_h)
        content_h = 300
    elif content_w >= content_h and content_w >= 300:
        content_h = (int)((content_h * 300) / content_w)
        content_w = 300
    
    content_img = content_img.resize((content_w, content_h), Image.ANTIALIAS)
    content_img.save(cf)
    
    isUploadStyle = request.form.get('is_upload_style')
    if isUploadStyle == 'true':
        style = request.files['style_img']
        sf = os.path.join(app.config['UPLOAD_FOLDER'], str(time.time()) + '_' + style.filename)
        style.save(sf)
        style.close()
        if sf[-3:] == 'png':
            im = Image.open(sf)
            rgb_im = im.convert('RGB')
            sf = sf[:-3] + 'jpg'
            rgb_im.save(sf)
    else:
        sf = SRC_FOLDER + request.form.get('style')
    style_img = Image.open(sf)
    style_img = style_img.resize(content_img.size, Image.ANTIALIAS)
    style_img.save(sf)


    model.initSession()
    rs = model.run_model(cf, sf)

    return Response(
        rs,
        mimetype="text/plain",
    )

if __name__ == '__main__':
    app.run(host='localhost', port=8001)