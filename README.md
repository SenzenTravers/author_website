# Site d'autrice

## TO-DO
-  Add PDF support for multiple chapters
-  Add HTML support for multiple chapters
-  Add buttons to filter rants

## Install it in o2switch
### Package

Pick Python 11.x.

> pip install -r requirements.txt
> pip install mysqlclient.

Indicate core/wsgi.py as the entrance point of your app.

Check that all migrations are applied.

You're done!

## Change staticfiles (images, CSS, etc)
1. Run `python manage.py collectstatic`
2. Restart the app

### Randoms
[CONVERT HTML TO PDF](https://doc.courtbouillon.org/weasyprint/stable/)

[CONVERT HTML TO PDF - PYTHON](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#python-library) => note que y a un argument pour gérer les pages !!

[pdf WITH A PAGE-AT RULE](https://developer.mozilla.org/en-US/docs/Web/CSS/@page)