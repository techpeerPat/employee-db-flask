# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /

# Copy the application directory contents into the container
COPY ./my_app/ /my_app/

# Install any needed packages specified in requirements.txt
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run the application with Gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "my_app.main:app"]
