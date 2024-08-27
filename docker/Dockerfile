# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the necessary Python packages
RUN pip install flask

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable

# Run app.py when the container launches
CMD ["python", "converter.py"]
