# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy dependencies file to work directory
COPY requirements.txt /code/

# Install dependencies
RUN python -m pip install -r requirements.txt

# Copy project in
COPY . /code/