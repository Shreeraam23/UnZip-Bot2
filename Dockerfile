# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the required dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the application
CMD ["python", "main.py"]
