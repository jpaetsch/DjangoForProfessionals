# Pull base image (host OS)
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# Copy dependencies file to working directory
COPY requirements.txt /code/

# Install dependencies
RUN python -m pip install -r requirements.txt

# Copy project in
COPY . /code/
