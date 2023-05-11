# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    gcc

# Install any needed packages specified in requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

# Define environment variable
ENV FLASK_APP app.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT 5000
ENV FLASK_RUN_HOST 0.0.0.0
# Make port 5000 available to the world outside this container
EXPOSE 5000
# Run app.py when the container launches
CMD ["flask", "run"]