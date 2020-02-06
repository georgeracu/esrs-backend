FROM python:3.7-alpine

RUN adduser -D nonroot

WORKDIR /home/nonroot

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app.py app.py
COPY start.sh ./
RUN chmod +x start.sh

ENV FLASK_APP app.py

RUN chown -R nonroot:nonroot ./
USER nonroot

EXPOSE 5000
ENTRYPOINT ["./start.sh"]