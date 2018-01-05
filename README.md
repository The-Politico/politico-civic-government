![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-civic-government

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-civic-government
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'government',
  ]
  ```

### Bootstrapping your database

**NOTE:** These commands must be run **AFTER** `bootstrap_geography` from the `django-politico-civic-geography` package.

##### Bootstrap the Federal Government

```
$ python manage.py bootstrap_fed
```

##### Bootstrap state jurisdictions

```
$ python manage.py bootstrap_jurisdiction
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
