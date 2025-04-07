#!/usr/bin/env bash

: "${MODULE_NAME:=configuration.wsgi}"  
: "${VARIABLE_NAME:=application}"  
: "${APP_MODULE:=$MODULE_NAME:$VARIABLE_NAME}"
: "${HOST:=0.0.0.0}"
: "${PORT:=8000}"

gunicorn --bind "$HOST:$PORT" "$APP_MODULE"
