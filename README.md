# Python Flask

![Test Python app](https://github.com/georgeracu/esrs-backend/workflows/Test%20Python%20app/badge.svg)
[![Build Status](https://dev.azure.com/azure0047/esrs-backend/_apis/build/status/georgeracu.esrs-backend?branchName=master)](https://dev.azure.com/azure0047/esrs-backend/_build/latest?definitionId=1&branchName=master)

## Table of Contents

- [Python Flask](#python-flask)
  - [Table of Contents](#table-of-contents)
  - [Development machine](#development-machine)
    - [Mac version](#mac-version)
      - [Install Python3 and dependencies](#install-python3-and-dependencies)
    - [Install Docker](#install-docker)
    - [Windows version](#windows-version)
      - [Install Python3](#install-python3)
      - [Install dependencies](#install-dependencies)
    - [Useful commands](#useful-commands)
    - [Other tools](#other-tools)
    - [Testing](#testing)
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

Install dependencies from `dev-requirements.txt`: `pip3 install -r requirements/dev-requirements.txt`.

Install all git hooks locally by running `python3 -m python_githooks`.

Tell Flask where is the entry point: `export FLASK_APP=app.py`. Required only if the app is used the default web server and then started with `flask run`.

Start the application: `gunicorn app:app`.

Et voila, you have a working Flask application.

Once finished with the virtual environment, you need to deactivate it: `deactivate`.

### Install Docker

Follow the installation steps described on the [official website](https://docs.docker.com/install/). Minimum version for Docker for Mac is `Docker version 19.03.5, build 633a0ea`.

### Windows version

This has been tested on `python 3.8.0`. If you have problems installing, check you are on this version.

#### Install Python3

- Python can be downloaded and installed from [this link](https://www.python.org/downloads/)

#### Install dependencies

- Download docker from [here](https://docs.docker.com/install/)
  - Leave UNIX file system on if asked.
- In `./scripts`, run `win_docker.bat`
- This should install the docker image and start the server.
  - If it fails, try removing the -d flag from the second command to run the server in the foreground.

### Useful commands

- Freeze dependencies and create requirements.txt: `pip3 freeze >requirements.txt`;
- Install dependencies from requirements.txt: `pip install -r requirements.txt`;
- Build a Docker image locally (you need to be in the root directory of the project): `docker build -t backend:latest .`.
- List all local Docker images: `docker images`. This should list your newly created image.
- Run locally your new image: `docker run --name backend -d -p 8000:5000 --rm backend:latest`. Now you can access the app at `http://localhost:8000/`.
- Run all tests: `coverage run -m unittest` or `python -m unittest`.
- View test coverage after running with coverage: `coverage report`.
- Run the application with one command: `FLASK_APP=app.py flask run` or to use _gunicorn_ `gunicorn app:app`.
  - `gunicorn` is **MAC only**. For development on Windows, the normal Flask environment is fine.
- Run linter: `flake8 app`.

### Other tools

- For linting and style guide enforcement we use [flake8](https://flake8.pycqa.org/en/latest/index.html). You can run it with `flake8 app`. Configuration file is `.flake8`.
- For git hooks, we use [python-githooks](https://github.com/ygpedroso/python-githooks). It has hooks defined in `.githooks.ini`. After updating a hook , you need to run `python -m python_githooks` in order to add new hooks.
  - Windows users - this must be executed in a bash environment, either through `git bash` or Windows' Linux subsystem.
- For code coverage we use [Coverage](https://coverage.readthedocs.io). It works based on `.coveragerc` config file.
- [Green Unicorn](https://gunicorn.org/#quickstart) as our production web server.

### Testing

For tests we use `unittest`. As a convention, it picks up all test files that are in directory `test/` and name starts with `test_`.

## Resources

- [Learning Flask](https://pythonise.com/series/learning-flask/your-first-flask-app)
- [Flask mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
