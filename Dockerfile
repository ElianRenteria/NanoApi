# Use a base image suitable for ARM architecture
FROM python:3.11-slim

# Set a working directory inside the container
WORKDIR /app

# Copy the requirements file if you have one (optional)
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask will run on
EXPOSE 8000

# Run the application with Gunicorn, using 3 workers for better concurrency
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "app:app"]

