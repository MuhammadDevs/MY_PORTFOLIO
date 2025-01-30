#!/bin/bash

# Exit on any error
set -o errexit  

# Install dependencies
pip install --upgrade pip  
pip install -r requirements.txt  

# Run database migrations
python manage.py migrate  

# Collect static files
python manage.py collectstatic --noinput  
