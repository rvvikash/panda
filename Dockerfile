FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port 8080
EXPOSE 8080

# Use gunicorn for production (better performance)
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app
