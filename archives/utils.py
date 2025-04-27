# from ebooklib import epub

from .models import Fic, Chapter
from .utils_constants import *


class FicDigester:
    def __init__(self, fic_id):
        self.fic = Fic.objects.get(id=fic_id)

    def return_title(self):
        return f"{self.fic.fic_title}_par_{self.fic.author}"

    def html_fic(self):
        fic = self.fic
        results = html_fic_base.format(
            title=fic.fic_title,
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
            title=fic.fic_title,
            author=fic.author,
            summary=fic.summary,
            chapters=self.pdf_chapter()
            )

        return results
    
    def epub_fic(self):
        fic = self.fic
        book = epub.EpubBook()
        book.set_title(fic.fic_title)
        book.set_language("fr")
        book.add_author(fic.author)
        chapters = self.epub_chapters()

        for chapter in chapters:
            book.add_item(chapter)

        if len(chapters) > 1:
            for chapter in enumerate(chapters, start=1):
                book.toc = (
                    epub.Link("chap_{number}.xhtml", "{number}.", "intro"),
                    (epub.Section(fic.fic_title), chapters),
                )

        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        return book

    # def epub_chapters(self):
    #     chapters = Chapter.objects.filter(
    #         fic=self.fic.id).order_by('id')
    #     formatted_chapters = []

    #     for number, chapter in enumerate(chapters, start=1):
    #         if chapter.title:
    #             chap = epub.EpubHtml(
    #                 title=chapter.title,
    #                 file_name=f"chap_{number}.xhtml",
    #                 lang="fr")
    #             chap.content = chapter.content
    #         else:
    #             chap = epub.EpubHtml(title=f"Chapitre {number}")
    #             chap.content = chapter.content

    #         formatted_chapters.append(chap)

    #     return formatted_chapters

