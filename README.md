# Let's Play Again Application

## Introduce

- Project name: Let's Play Again
- Detail: 
    - Choose place to go to cultural events, parks, kidscafes, toylibraries with your children
    - Select a category
    - Then, it shows the information of the events that fit the category

## Requirements

- Python (3.6)
- pipenv
- Django (2.x)
- pyproj

### Secrets

#### '.secrets/base.json'

```json
{
  "SECRET_KEY": "<Django secret key>",
  "CULTURE_API_CLIENT_KEY": "<Your Authentication key of data.seoul.go.kr>"
}

```

#### '.secrets/dev.json'
```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "<Postgresql>",
      "NAME": "<your psql database name>",
      "USER": "<owner name of psql database>",
      "PASSWORD": "<your password>",
      "HOST": "<your host>",
      "PORT": ""
    }
  }
}
```

## Running

```
# Move project's directory
- pipenv install
- pipenv shell
- cd app
- export DJANGO_SETTINGS_MODULE=config.settings.dev
./manage.py runserver
```

## ETC

- If you failed install pyproj
    - You'll probably have to install PROJ.4
    - [PROJ.4 Document](https://docs.djangoproject.com/ko/2.1/ref/contrib/gis/install/geolibs/#id9)


