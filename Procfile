web: gunicorn hangout.config.settings.config.wsgi:application
worker: celery worker --app=hangout.taskapp --loglevel=info
