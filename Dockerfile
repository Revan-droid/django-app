FROM python:3.10

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN python manage.py makemigrations 

COPY . /app 

CMD [ "python","manage.py","runserver" ]