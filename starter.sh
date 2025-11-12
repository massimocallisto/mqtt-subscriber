#!/bin/sh

source venv/bin/activate

export SERVER_ADDR=localhost
export PORT=1883
#export USERNAME=
#export PASSWORD=
export TOPIC=#

if [ -f ".env" ]; then
  echo "override variables from .env file"
  source .env
fi

python app.py