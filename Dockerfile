# Use the Python 3.11.1 image as the base image
FROM python:3.11.1
# Set an environment variable to ensure that Python output is not buffered
ENV PYTHONUNBUFFERED 1
# Set the working directory inside the container to /app/backend
WORKDIR /app/backend
# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/backend/
# Install Python dependencies based on the requirements.txt file
RUN pip install -r requirements.txt
# Copy the entire local directory into the working directory
COPY . /app/backend/
# Expose port 8000 to allow external connections
EXPOSE 8000

#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# Define the entry point script to be executed when the container starts
ENTRYPOINT ["/app/backend/django.sh"]