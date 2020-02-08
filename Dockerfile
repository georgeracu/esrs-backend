FROM python:3.7-alpine

RUN adduser -D nonroot

WORKDIR /home/nonroot

COPY requirements/common-requirements.txt common-requirements.txt
COPY requirements/prod-requirements.txt prod-requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r prod-requirements.txt
RUN venv/bin/pip install gunicorn

COPY app/ app/
COPY start.sh ./
RUN chmod +x start.sh

ENV FLASK_APP app.py

RUN chown -R nonroot:nonroot ./
USER nonroot

EXPOSE 5000
ENTRYPOINT ["./start.sh"]