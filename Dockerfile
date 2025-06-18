FROM python:3.11-alpine

# Set work directory
WORKDIR /app

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables (optional, for UTF-8)
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

# Entrypoint to run the main script
ENTRYPOINT ["python", "main.py"]