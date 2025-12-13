from archives.models import Chapter

from .common_utils import return_chapter_title, return_html_chapter_title
from .epub_bases import html_chapter


class EpubMaker:
    def __init__(
        self, story
    ):
        self.story = story
        self.epub_file = self.return_story()

        
    def generate_ebook(self):
        self.add_chapters()

        return self.write_epub_to_memory(self.epub_file)
        # self.epub_file.create(f"{self.story.fic_title}.epub")

    def return_story(self):        
        return pypub.Epub(
            title=self.story.fic_title,
            creator=self.story.author.nickname,
            language="fr",
            rights="Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International",
            publisher="Voiture Noire",
            date=self.story.date,
        )
    
    def add_chapters(self):
        chapters = Chapter.objects.filter(
            fic=self.story.id).order_by('id')

        i = 1

        if len(chapters) == 1:
            formatted_chapter = html_chapter.format(
                numbered_chapter_title="",
                chapter_content=chapter.content
            )
            content = pyxml.html.tostring(formatted_chapter)
            content = formatted_chapter
            chapter = pypub.create_chapter_from_text(content)
            assign  = self.epub_file.add_chapter(chapter)
        else:
            for chapter in chapters:
                chapter_title_html = return_html_chapter_title(chapter, i)
                formatted_chapter = html_chapter.format(
                    numbered_chapter_title=chapter_title_html,
                    chapter_content=chapter.content
                )
                content = formatted_chapter.encode('utf-8')
        
                chapter_title = return_chapter_title(chapter, i)
                chapter = pypub.create_chapter_from_html(content, title=chapter_title)
                assign  = self.epub_file.add_chapter(chapter)

                i += 1