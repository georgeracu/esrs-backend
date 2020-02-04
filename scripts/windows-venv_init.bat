@ECHO Go up to root
cd ..

ECHO@ Install the prereqs
pip install virtualenv
virtualenv venv

@ECHO Start the virtual environment

call venv/Scripts/activate

@ECHO Install dependencies in the venv

pip install -r requirements.txt
set FLASK_APP=app.py

@ECHO Done! You can now start the server with `flask run`

cmd /k
