![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# government

### Quickstart

1. Install the app.

  ```
  $ pip install government
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'government',
  ]

  #########################
  # government settings

  GOVERNMENT_SECRET_KEY = ''
  GOVERNMENT_AWS_ACCESS_KEY_ID = ''
  GOVERNMENT_AWS_SECRET_ACCESS_KEY = ''
  GOVERNMENT_AWS_REGION = ''
  GOVERNMENT_AWS_S3_BUCKET = ''
  GOVERNMENT_CLOUDFRONT_ALTERNATE_DOMAIN = ''
  GOVERNMENT_S3_UPLOAD_ROOT = ''
  ```

### Developing

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```

Developing static assets? Move into the pluggable app's staticapp directory and start the node development server, which will automatically proxy Django's development server.

  ```
  $ cd government/staticapp
  $ gulp
  ```

Want to not worry about it? Use the shortcut make command.

  ```
  $ make dev
  ```

##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to the `.env` file.

  ```
  DATABASE_URL="postgres://localhost:5432/government"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```
