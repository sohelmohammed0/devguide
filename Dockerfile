# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables for a more secure and efficient container
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Create a non-root user for security, and give permissions to /app
RUN adduser --disabled-password appuser && \
    chown -R appuser /app
USER appuser

# Expose the application port
EXPOSE 5000

# Define the default command to run the application
CMD ["python", "app.py"]
