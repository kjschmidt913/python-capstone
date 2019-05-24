# python-capstone
Final capstone project for [Udemy's Complete Python Bootcamp: Go from zero to hero in Python 3](https://www.udemy.com/complete-python-bootcamp/)

## Overview:
A web app that randomly chooses Ariana Grande lyrics and overlays them onto inspirational images. Lyrics are chosen from Grande's albums Sweetener and Thank U, Next. I was unable to find a free lyrics API that had the selection I was looking for and was reliable so I created my own database of lyrics, which can be found in `mysite/polls/models.py`. This is my first web app created with Django. I followed the [tutorial](https://docs.djangoproject.com/en/2.2/intro/) in the documentation, which explains the filenames and organization.

## Built with:
* [Django](https://www.djangoproject.com/)
* Python
* [Bootstrap v4.3.1](https://getbootstrap.com/)

## Running locally:
### Prerequisites:
Make sure Python, pip, and Django are already installed. If not, go [here](https://docs.djangoproject.com/en/2.2/topics/install/). Understand how to run your [virtual environment](https://docs.djangoproject.com/en/2.2/intro/contributing/#getting-a-copy-of-django-s-development-version).

### Getting started:
Once you've cloned the repository, run your virtual environment. Then run the server with the command `python manage.py runserver`. The app will be found on http://127.0.0.1:8000/polls/
