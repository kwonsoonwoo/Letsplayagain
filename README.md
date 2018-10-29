# Let's Play Again Application

## Introduce

- Project name: Let's Play Again
- Detail: 
    - Choose place to go to cultural events, parks, kidscafes, toy libraries with your children
    - Select a category
    - Then, it shows the information of the events that fit the category

## Requirements

- Python (3.6)
- pipenv
- Django (2.x)

### Secrets

#### '.secrets/base.json'

```json
{
  "SECRET_KEY": "<Django secret key>"
}
```

## Running

```
# Move project's directory
- pipenv install
- pipenv shell
- cd app
- export DJANGO_SETTINGS_MODULE=config.settings.local
./manage.py runserver
```


