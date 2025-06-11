FROM python:3.13-slim
RUN useradd -u 1001 flaskuser
WORKDIR /app
COPY . .
COPY ./templates/index.html /app/templates/
RUN pip install -no-cache-dir -r requirements.txt 
EXPOSE 8080
USER flaskuser
CMD ["python", "converter.py"]
