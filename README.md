# django-heroku-worker

- git push heroku main
- heroku run python manage.py migrate
- heroku addons:create redistogo
- heroku scale worker=1
- heroku run worker
