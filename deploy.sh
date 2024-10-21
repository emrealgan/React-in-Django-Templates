#!/bin/bash

cd /home/ubuntu/React-in-Django-Templates || exit
git pull origin main

# Create a new virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Restart services
sudo systemctl restart gunicorn
sudo systemctl restart nginx
