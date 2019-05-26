# Neural Style Transfer App

This is a webapp using neural style transfer model.

To use this app, you need to upload 2 images, one is content image and other is style image.

It will take a while to create a new image which is combined of input images.

## Installation

Create a virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Show dependencies

```bash
pip list
```


Download pretrained model

https://drive.google.com/file/d/1XQ2pTh7heTevGnUNkgeq5PxEGFfD1wPr/view?usp=sharing

Save it in `src/pretrained-model/`

## Run model

```bash
python3 src/model.py
```

## Run flask app

```bash
python3 src/upload.py
```
This command will start a development server at http://localhost:8001

## Deactivate

When you are done working in the virtual environment for the moment, you can deactivate it

```bash
deactivate
```