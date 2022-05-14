#!/bin/sh

RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m'

python manage.py check --deploy
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

if [ "$DEBUG" = "True" ]; then
  printf "${RED}WARNING!!!${NC}   ${BLUE}Debug is True. You need set False for deployment${NC}"
fi

if [ "$1" = 'gunicorn' ] && [ -z "$GUNICORN_CMD_ARGS" ]; then
    b="--bind=0.0.0.0:${DJANGO_PORT}"
    conf="-c gunicorn.config.py"
    export GUNICORN_CMD_ARGS=b,conf
    echo "\n${GREEN}Starting gunicorn with args: $b $conf\n"
    exec "$@" $b $conf
else
    exec "$@"
fi
