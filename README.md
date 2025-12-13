# Site d'autrice

1. [TO-DO](#to-do)
   - [Must-have](#must-have)
   - [Nice to have](#nice-to-have)
   - [Last priority](#last-priority)
2. [Using the app locally](#local-use)
   - [Installing the app](#installing)
   - [Launching the app](#launching)
   - [Good practices](#good-practices)
3. [Setting the app in o2switch (our heberger)](#setting-the-app-in-o2switch)
4. [Credits](#credits)
5. [Useful commands](#useful-commands)
6. [Random notes](#random-notes)


## TO-DO
### Must-have
- [VOITURE_NOIRE] A Json view that Eriza would be able to ping
- [SERVER] Add events (ongoing: lack a get view, post view, edit view, delete view)
- [SERVER] Add a birthday (ongoing: lacking form implementation)
- [STORIES] Post comment (ongoing: lacking view + checks)
- [STORIES] Delete chapter
- [STORIES] Add PDF thanks to [this library](https://www.geeksforgeeks.org/creating-ebooks-with-borb-in-python/).
available [here](https://github.com/jorisschellekens/borb?tab=readme-ov-file). Instruction book can be found
[here](https://github.com/jorisschellekens/borb-examples/tree/master/chapter_001).
- [STORIES] Add PDF support for multiple chapters

### Nice to have
- [WRITER] Add buttons to filter rants
- [PROMPTS] Search prompts through text
- [STORIES] Handle last_updated field

### Last priority
- [PINE] (Mobile) : Rearrange banner
- [PINE] (Mobile) Mobile : 50 % of page as a mosaic
- [PINE] (Computer) Commissions : final page
- [PINE] (Mobile) Commissions : final page
- [PROMPTS] Properly implement [error messages](https://docs.djangoproject.com/en/5.1/ref/contrib/messages/)
- [ENV] upgrading python  >= 3.13 needs to upgrade cffi to >= 1.17.1 also

## LOCAL USE

### Installing
This app was tested with Python 3.11 and Python 3.12.3. Other versions were not tested.

FOR UNIX : navigate to the project's root folder from your command line
 interface, then:

``` bash
# Create a virtual environment with the command:
python -m venv venv

# Activate it
source venv/bin/activate

# Install necessary packages:
pip install -r requirements.txt
```

If it complains that you need to install mssql... Remove the line from your
version of requirements.txt, then try again. Mssql is only used in production.

Then, run:
``` bash
# Create migrations, i.e. ORM-generated files.
# pay attention that the folder migrations should exists 
# its currenting ignore by git (see .gitignore file)
# can cause issue like: 
# 'CommandError: Unable to serialize database: no such table: voiture_noire_discordprofile'
python manage.py makemigrations
python manage.py migrate

# Create your superuser, i.e. your admin profile.
# Do not put in a real mail address.
python manage.py createsuperuser --username=jean --email=jean@example.com
```

You can now launch the app!

### Launching
``` bash
python manage.py runserver
```

Boom.

The app should be launched from `http://127.0.0.1:8000/`; you can go to 
`http://127.0.0.1:8000/admin/` for admin options.

### Good practices
We try to preface commits with "feat", "fix", or "chore" for clarity's sake. Do let me know 
if you have other preferences.

We use [PEP 8](https://peps.python.org/pep-0008/) for Python. If wished, I can include a linting 
library in our packages, such as [Flake8](https://flake8.pycqa.org/en/latest/) or 
[Black](https://pypi.org/project/black/).

There are tests available, though not all pages or functions are tested because the tests were 
added late and this is done with my spare energy and/or I'm a terrible human being.

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

## Credits
[Rich text editor](https://codepen.io/BibekOli/pen/abRgbVW)


## Useful commands
To export the db, app by app, into a json format suitable for fixture:
`python manage.py dumpdata voiture_noire --settings=core.settings > voiture_noire/fixtures/voiture_noire.json`

To run the tests specific to one particular TestCase:
`python manage.py test tests.test_voiture_noire.VoitureNoireTestCase`
`python manage.py test tests.test_library.LibraryTestCase`

(In prod) To run statics and clear them, in case the files got corrupted (don't forget to restart afterwards!):
`python manage.py collectstatic --clear`

## Random notes
[CONVERT HTML TO PDF](https://doc.courtbouillon.org/weasyprint/stable/)

[CONVERT HTML TO PDF - PYTHON](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#python-library) => note que y a un argument pour gérer les pages !!

[pdf WITH A PAGE-AT RULE](https://developer.mozilla.org/en-US/docs/Web/CSS/@page)

[BIBLIOTHÈQUE POUR RACCOURCIS](https://www.npmjs.com/package/hotkeys-js)

[PLAY A SOUND WHEN KEY IS PRESSED](https://stackoverflow.com/questions/12578379/play-a-sound-when-a-key-is-pressed)

[INSTANCE OF RICH TEXT EDITOR](https://codingtorque.com/rich-text-editor-using-javascript/)

