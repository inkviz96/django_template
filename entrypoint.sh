#!/bin/sh


python manage.py check --deploy
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

if [ "$1" = 'gunicorn' ] && [ -z "$GUNICORN_CMD_ARGS" ]; then
    b="--bind=0.0.0.0:${DJANGO_PORT}"
    conf="-c gunicorn.config.py"
    export GUNICORN_CMD_ARGS=b,conf
    echo "\nStarting gunicorn with args: $b $conf\n"
    exec "$@" $b $conf
else
    exec "$@"
fi
