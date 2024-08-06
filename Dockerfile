FROM python:3.11-slim-buster

WORKDIR /usr/app

COPY ./ /usr/app

RUN pip install -r requirements.txt && pip install -U google-generativeai

CMD ["python", "main.py"]