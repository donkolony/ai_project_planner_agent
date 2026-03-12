#!/bin/bash

# Azure App Service Startup Script for Python FastAPI

set -e

echo "Starting AI Project Planner Backend..."

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Initialize database (create tables if they don't exist)
echo "Initializing database..."
python -c "from app.core.database import init_db; init_db()"

# Start the application using gunicorn with uvicorn workers (recommended for Azure)
echo "Starting uvicorn server..."
gunicorn app.main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --timeout 60
