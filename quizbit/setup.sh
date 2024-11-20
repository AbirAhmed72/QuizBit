#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install Python3 to proceed."
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

# Seed the database
echo "Seeding the database with initial data..."
python manage.py seed_data

# Start the development server
echo "Starting the development server..."
python manage.py runserver
