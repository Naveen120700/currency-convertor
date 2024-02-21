# Dockerfile
FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /currency_convertor

COPY currency_convertor/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY currency_convertor .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]