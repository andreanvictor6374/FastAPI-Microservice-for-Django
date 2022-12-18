[![FastAPI Microservice for Django](https://static.codingforentrepreneurs.com/media/projects/fastapi-microservice-django/images/share/FastAPI_Microservice_for_Try_Django.jpg)](https://www.codingforentrepreneurs.com/projects/fastapi-microservice-django)


Learn to deploy a FastAPI application into production DigitalOcean App Platform. This is a microservice for our [Try Django 3.2](https://www.codingforentrepreneurs.com/projects/try-django-3-2) project. The goal is to extract any and all text from images using a technique called OCR.

Here's a list of the packages we will use to accomplish this:

- FastAPI
- Tesseract OCR
- pytesseract
- pre-commit
- pytest
- Gunicorn
- Uvicorn
- Requests
- Docker
- and more

## Want to just run the app?
Click below to deploy to DigitalOcean. Be sure to grab your $100 credit [here](https://do.co/cfe-github).


[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/codingforentrepreneurs/FastAPI-Microservice-for-Django/tree/main)


## to tun locally
```shell
uvicorn app.main:app --reload
```

## Generate token
```python
import secrets
secrets.token_urlsafe(32)
```

## test 
```shell
pytest -s
```

## error
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
```shell
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
# solution 
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```