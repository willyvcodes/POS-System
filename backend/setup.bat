@echo off

echo RUNNING FASTAPI BACKEND

set dir_venv="venv"

IF exist %dir_venv% (
    echo ... A VIRTUAL ENVIRONMENT ALREADY EXISTS
) ELSE (
    echo BUILDING VIRTUAL ENVIRONMENT
    CALL python -m venv %dir_venv%
)

echo ACTIVATING VIRTUAL ENVIRONMENT
CALL venv\Scripts\activate.bat

echo INSTALLING DEPENDENCIES
pip install -r requirements.txt

echo RUNNING SERVER
uvicorn main:app --reload
@REM uvicorn main:app --reload ssl_keyfile="./key.pem" ssl_certfile="./cert.pem"