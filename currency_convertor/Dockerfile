# Dockerfile
FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /currency_convertor

RUN mkdir "static"

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

RUN pip install flake8
#RUN flake8 .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]