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

## TODO
### PROMPTS
- TODO: le POST sur la page de prompt ne poste plus un prompt (l'adresse du postage de prompt sera changée). Elle prend en compte un (1) paramètre qui servira à trier les prompts.
- Properly implement error messages https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
  Petit script pour welcome-blurb
- ROFIL(Voiture Noire): messages d'erreur si ça foire/blocage avec nombre maximum de charactères
- Dans un futur monde idéal : like/dislikes en rich text editor 
- Une joulie bannière
- PROMPTS(Voiture Noire): introduire option de recherche sur le texte des prompts
- PROMPTS(Voiture Noire): introduire tri sur les prompts
- PROMPTS(Voiture Noire): page éditer mes histoires fonctionnelle
- la lecture annotée ? À la lecture, on peut ajouter des commentaires à chaque paragraphe (ou lettre ?). Le résultat est enregitré pour envoi à l'autrice ? 

- When time is selected, then start sprint upon pressing Enter key
- PINE(Mobile) : réarranger la bannière
- PINE(Mobile) Mobile : 50 % de la page est une mosaïque
- PINE(Ordinateur) Commissions : page complète
- PINE(Mobile) Commissions : page complète

### Randoms
[CONVERT HTML TO PDF](https://doc.courtbouillon.org/weasyprint/stable/)

[CONVERT HTML TO PDF - PYTHON](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#python-library) => note que y a un argument pour gérer les pages !!

[pdf WITH A PAGE-AT RULE](https://developer.mozilla.org/en-US/docs/Web/CSS/@page)

[BIBLIOTHÈQUE POUR RACCOURCIS](https://www.npmjs.com/package/hotkeys-js)

[PLAY A SOUND WHEN KEY IS PRESSED](https://stackoverflow.com/questions/12578379/play-a-sound-when-a-key-is-pressed)

[INSTANCE OF RICH TEXT EDITOR](https://codingtorque.com/rich-text-editor-using-javascript/)

## Credit
[Rich text editor](https://codepen.io/BibekOli/pen/abRgbVW)

