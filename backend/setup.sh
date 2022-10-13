#!/bin/bash

echo "RUNNING FASTAPI BACKEND"

dir_venv="venv"

if [ ! -d "$dir_venv" ]
    echo "... A VIRTUAL ENVIRONMENT ALREADY EXISTS"
then
    echo "BUILDING VIRTUAL ENVIRONMENT"
    python3 -m venv $dir_venv
fi

echo "ACTIVATING VIRTUAL ENVIRONMENT"
source ./venv/bin/activate

echo "... UPGRADE PIP"
pip3 install --upgrade pip

echo "INSTALLING DEPENDENCIES"
pip3 install -r requirements.txt

echo "RUNNING SERVER"
uvicorn main:app --reload