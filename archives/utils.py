# import pypub

from .models import Fic, Chapter
from .utils_constants import *


class FicDigester:
    def __init__(self, fic_id):
        self.fic = Fic.objects.get(id=fic_id)

    def return_title(self):
        return f"{self.fic.title}_par_{self.fic.author}"

    def html_fic(self):
        fic = self.fic
        results = html_fic_base.format(
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

    def pdf_chapter(self):
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

    def pdf_fic(self):
        fic = self.fic
        results = pdf_fic_base.format(
            pdf_page_title_style=pdf_page_title_style,
            pdf_normal_page_style=pdf_normal_page_style,
            title=fic.title,
            author=fic.author,
            summary=fic.summary,
            chapters=self.pdf_chapter()
            )

        return results