# Honeypot

This repo is to help manage an SSH honeypot. The website is intended to run
on the honeypot and will allow viewing live data.

## Install

```
# Load database
python manage.py migrate
python manage.py loaddata settings
```