FROM python:3.11-slim

WORKDIR /app

# Prevent Python from writing bytecode and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY app/ ./app/
COPY static/ ./static/

# Default fallback port (Render dynamically sets $PORT)
EXPOSE 8000

# Start server binding dynamically to $PORT (or fallback to 8000)
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}