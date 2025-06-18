FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user and set permissions
RUN useradd -m appuser && chown -R appuser /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .
RUN chown -R appuser /app

# Set environment variables (optional, for UTF-8)
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

# Switch to non-root user
USER appuser

# Entrypoint to run the main script
ENTRYPOINT ["python", "main.py"]
CMD []