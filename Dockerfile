# Use the official Python image as the base image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the client and server Python scripts to the container
COPY client.py .
COPY server.py .

# Expose the port that the server will listen on
EXPOSE 8000

# Start the server when the container is run
CMD ["python", "server.py"]
