FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirments.txt /app

RUN pip inatall --upgrade pip
RUN pip install -r requirments.txt

COPY ./core /app

CMD ["python","manage.py","runserver","0.0.0.0:8000"]