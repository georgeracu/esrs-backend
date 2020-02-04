REM Go up to root
cd ..

REM Install the prereqs
pip install virtualenv
virtualenv venv

REM Start the virtual environment
call venv/Scripts/activate

REM Install dependencies in the venv
pip install -r requirements.txt

REM Set the entry point
set FLASK_APP=app.py

ECHO Done! You can now start the server from the venv
@PAUSE