# Site d'autrice

## TO-DO
### Must-have
- [STORIES] Delete chapter
- [STORIES] Add PDF
- [STORIES] Add HTML
- [STORIES] Add PDF support for multiple chapters
- [STORIES] Add HTML support for multiple chapters

### Nice to have
- [WRITER] Add buttons to filter rants
- [PROMPTS] Search prompts through text
- [STORIES] Handle last_updated field
- [BLACK CAR] Small, funny script to handle welcome-blurb

### Last priority
- [PINE] (Mobile) : Rearrange banner
- [PINE] (Mobile) Mobile : 50 % of page as a mosaic
- [PINE] (Computer) Commissions : final page
- [PINE] (Mobile) Commissions : final page

## Setting the app in o2switch
### Package

Pick Python 3.11.x.

> pip install -r requirements.txt
> pip install mysqlclient.

Indicate core/wsgi.py as the entrance point of your app.

Check that all migrations are applied.

### Change staticfiles (images, CSS, etc)
1. Run `python manage.py collectstatic`
2. Restart the app

### When making changes
1. If on the front end: run `python manage.py collectstatic`, then restart
2. If involving models: run migrations

### PROMPTS
- Properly implement error messages https://docs.djangoproject.com/en/5.1/ref/contrib/messages/


### Randoms
[CONVERT HTML TO PDF](https://doc.courtbouillon.org/weasyprint/stable/)

[CONVERT HTML TO PDF - PYTHON](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#python-library) => note que y a un argument pour gérer les pages !!

[pdf WITH A PAGE-AT RULE](https://developer.mozilla.org/en-US/docs/Web/CSS/@page)

[BIBLIOTHÈQUE POUR RACCOURCIS](https://www.npmjs.com/package/hotkeys-js)

[PLAY A SOUND WHEN KEY IS PRESSED](https://stackoverflow.com/questions/12578379/play-a-sound-when-a-key-is-pressed)

[INSTANCE OF RICH TEXT EDITOR](https://codingtorque.com/rich-text-editor-using-javascript/)

## Credit
[Rich text editor](https://codepen.io/BibekOli/pen/abRgbVW)


## Useful commands
To export the db, app by app, into a json format suitable for fixture:
`python manage.py dumpdata voiture_noire --settings=core.settings > voiture_noire/fixtures/voiture_noire.json`

To run the tests specific to one particular TestCase:
`python manage.py test tests.test_voiture_noire.VoitureNoireTestCase`
`python manage.py test tests.test_library.LibraryTestCase`

(In prod) To run statics and clear them, in case the files got corrupted (don't forget to restart afterwards!):
`python manage.py collectstatic --clear`
