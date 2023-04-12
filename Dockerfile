FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential

RUN  apt-get update && \
     pip install -r requirements.txt

COPY ./fast_app /fast_app