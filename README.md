# esrs-backend
Python

### Table of Contents

- [Setup a development machine](#development-machine)
    - [Mac version](#mac-version)
    - [Useful commands](#useful-commands)

## Development Machine

Windows and Apple devices have different configuration. For an Apple device, Python 3 is known as `python3`, therefore pip is also known as `pip3`.

### Mac Version

To install Python 3 and its dependencies, we will use Homebrew. You can install Homebrew from [here](https://brew.sh/).

#### Install Python3 and dependencies

`brew install python3`

To check if it was installed, just run `python3 --version`.

Install virtualenv: `pip3 install virtualenv`.

Go to esrs-backend and start venv: `virtualenv venv`

After installing the virtualenv, then you need to activate it: `source venv/bin/activate`.

While in the virtual environment, you need to install Flask: `pip3 install flask==1.1.1`.

Install dependencies from `requirements.txt`: `pip3 install -r requirements.txt`

Tell Flask where is the entry point: `export FLASK_APP=app.py`.

Start the application: `flask run`.

Et voila, you have a working Flask application.

Once finished with the virtual environment, you need to deactivate it: `deactivate`.

### Useful commands

* Freeze dependencies and create requirements.txt: `pip3 freeze >requirements.txt`;
* Install dependencies from requirements.txt: `pip install -r requirements.txt`;
