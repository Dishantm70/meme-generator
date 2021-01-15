# Meme generator app built with Django and Angular.js

## Steps to run locally:
1. Install python dependencies: `pip install requirements.txt`
2. Migrate the database: `./manage.py migrate`
3. Run local server on poer 8000: `./manage.py runserver`

- The application used Django Rest Framework. The documentation for all APIs can be found on [This link](https://documenter.getpostman.com/view/9395373/TVzVhaqG).

- The App is dockerized and deployed on Google Cloud Run and can be accessed on : [This link](https://meme-generator-nj3al6s2ja-el.a.run.app/).

- Local development uses sqlite3 database and the deployed application uses Cloud SQL(Postgres 12) database.

- Continuous deployment has been set up with Github using Google Cloud Build. Every commit on "main" branch get deployed automatically within a couple of minutes.