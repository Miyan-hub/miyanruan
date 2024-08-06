FROM python:3.11-slim-buster

WORKDIR /usr/app

COPY ./ /usr/app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]