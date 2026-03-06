#FROM python:3.9-slim

#WORKDIR /app

#COPY app.py .

#RUN mkdir -p /data

#CMD ["python", "app.py"]

FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

CMD ["python", "app.py"]
