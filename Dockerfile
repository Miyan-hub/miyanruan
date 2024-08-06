FROM python:3.11-slim-buster

WORKDIR /usr/app

COPY ./ /usr/app

CMD ["python", "main.py"]