FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin && rm -rf /var/lib/apt/lists/*
RUN mkdir /django_app
COPY ./app/ /django_app/
WORKDIR /django_app
RUN pip install -r requirements.txt
