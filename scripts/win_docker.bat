cd ..
docker build -t backend:latest .
docker run --name backend -p 8000:5000 --rm backend:latest
@PAUSE