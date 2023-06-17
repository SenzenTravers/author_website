# import pypub

from .models import Fic, Chapter


base_fic = """<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="Senestre-Coquecigrues">
        <title>{title}, par {author}</title>

    </head>

    <body style="background-color: #fffffa">
        <section style="border: black thin solid; padding: 1.4em; margin: 1em; margin-bottom: 4em;">
            <header style="text-align: center">
                <h1 style="font-size: 3em; margin-bottom: 0px">{title}</h1>
                <p style="font-size: 1.8em; margin-top: 0px">par {author}</p>
            </header>

            <div text-align: justify><i>{summary}</i></div>
        </section>

    {chapters}
    </body>
</html>"""

numbered_chapter_title = """<h2 style="margin-top: 2em">Chapitre {number}</h2>"""
class FicDigester:
    def __init__(self, fic_id):
        self.fic = Fic.objects.get(id=fic_id)

    def return_title(self):
        return f"{self.fic.title}_par_{self.fic.author}"

    def html_fic(self):
        fic = self.fic
        results = base_fic.format(
            title=fic.title,
            author=fic.author,
            summary=fic.summary,
            chapters=self.html_chapter()
        )

        return results
    
    def html_chapter(self):
        chapters = Chapter.objects.filter(
            fic=self.fic.id).order_by('id')
        formatted_chapters = []
        i = 1

        if len(chapters) == 1:
            return chapters[0].content
        else:
            for chapter in chapters:
                formatted_chapters.append(
                    numbered_chapter_title.format(number=i) + chapter.content
                    )
                i += 1

            return "".join(formatted_chapters)

    # def epub_fic(self):
    #     all_chapters = self.html_chapter()
    #     epub_book = pypub.Epub("self.return_title()")

    #     if type(all_chapters) == str:
    #         chap = pypub.create_chapter_from_text("bob")
    #         epub_book.add_chapter("chap")
    #     else:
    #         for chap in all_chapters:
    #             chap = pypub.create_chapter_from_text(chap)
    #             epub_book.add_chapter(chap)

    #     epub_book.create('./my-first-epub.epub')


# class FicDigester:
#     def __init__(self):
#         # ID to call to DB and return a Chapter and Fic Object
#         print("Nothing")

#     def create_file(self, data):
#         # Later, need a format_for_html thing
#         # Infos to format stuff
#         title, path = tempfile.mkstemp(suffix=".html", text=True)

#         fic = str.encode(data, "utf-8")
#         os.write(title, fic)
#         try:
#             self.download_file(request)
#         except Exception as e:
#             print(e)

#         os.close(title)
#         os.remove(path)

#     def download_file(self, request):
#         fic = "/tmp/tmps0y34d_0.html"
#         resp = HttpResponse('')

#         with  open(fic, 'r') as tmp:
#             filename = tmp.name.split('/')[-1]
#             resp = HttpResponse(tmp, content_type='application/text;charset=UTF-8')
#             resp['Content-Disposition'] = "attachment; filename=%s" % filename

#         return resp


