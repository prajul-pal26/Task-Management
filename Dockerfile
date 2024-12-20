# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
