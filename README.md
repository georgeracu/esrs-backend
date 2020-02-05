# esrs-backend

Python

## Table of Contents

- [esrs-backend](#esrs-backend)
  - [Table of Contents](#table-of-contents)
  - [Development machine](#development-machine)
    - [Mac version](#mac-version)
      - [Install Python3 and dependencies](#install-python3-and-dependencies)
    - [Windows version](#windows-version)
      - [Install Python3](#install-python3)
      - [Install dependencies](#install-dependencies)
      - [Known issues](#known-issues)
    - [Useful commands](#useful-commands)
  - [Resources](#resources)

## Development machine

Windows and Apple devices have different configuration. For an Apple device, Python 3 is known as `python3`, therefore pip is also known as `pip3`.

### Mac version

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

### Windows version

This has been tested on `python 3.8.0`. If you have problems installing, check you are on this version.

#### Install Python3

- Python can be downloaded and installed from [this link](https://www.python.org/downloads/)

#### Install dependencies

- In `esrs-backend/scripts`, run `windows-venv_init.bat`
- This should:
  - Install `virtualenv` through `pip`
  - Activate the virtual environment
  - Install dependencies from `requirements.txt`
  - Set the entrypoint
- Run `flask run` to start the server on localhost

#### Known issues

- If you get `'virtualenv' is not recognized as an internal or external command...`:
  - Make sure your python `%PATH%` is set
  - Run `pip install --upgrade --force virtualenv` in cmd
  - Run the script again

### Useful commands

- Freeze dependencies and create requirements.txt: `pip3 freeze >requirements.txt`;
- Install dependencies from requirements.txt: `pip install -r requirements.txt`;

## Resources

- [Learning Flask](https://pythonise.com/series/learning-flask/your-first-flask-app)
- [Flask mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
