FROM python:3.9-slim

WORKDIR /consumer
COPY . .

RUN pip install -r requirements.txt

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "microservice:app" ]
