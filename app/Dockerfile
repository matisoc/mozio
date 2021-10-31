# Builder

FROM python:3.9.6-alpine as builder

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev gdal
RUN pip install --upgrade pip
COPY . .
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Release

FROM python:3.9.6-alpine

RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME
RUN apk update && apk add --no-cache \
                        --upgrade \
                        alpine-sdk \
                        libffi-dev \
                        jpeg-dev \
                        zlib-dev \
                        musl-dev \
                        libffi \
                        postgresql-dev \
                        gdal-dev \
                        geos-dev  \
                        postgresql-libs \
                        && apk add --virtual .build-deps postgresql-libs 
 
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh
COPY . $APP_HOME
RUN chown -R app:app $APP_HOME
USER app
ENTRYPOINT ["/home/app/web/entrypoint.sh"]