html_fic_base = """<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="{author}">
        <title>{title}, par {author}</title>

    </head>

    <body style="background-color: #fffffa; padding: 15%; padding-top: 0.5em; line-height: 2em;text-indent: 2em">
        <section style="border: black thin solid; padding: 2em; margin: 1em; margin-bottom: 4em;text-indent: 2em">
            <header style="text-align: center">
                <h1 style="font-size: 3em; margin-bottom: 0px;line-height: normal;">{title}</h1>
                <p style="font-size: 1.8em; margin-top: 0px">par {author}</p>
            </header>

            <div style="text-align: justify;"><i>{summary}</i></div>

        </section>

    {chapters}
    </body>
</html>"""