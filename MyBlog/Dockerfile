# Use an official Python runtime as a parent image
FROM python:3.11.6-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

COPY ./media/profile_pics/default.png ./code/media/profile_pics/
COPY ./media/profile_pics/signalBlueDark.png ./code/media/profile_pics/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8080