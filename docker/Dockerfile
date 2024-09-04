FROM python:3.12-slim

WORKDIR /app

COPY converter.py /app/
COPY ./templates/index.html /app/templates/

RUN pip install flask

EXPOSE 8080

CMD ["python", "converter.py"]
