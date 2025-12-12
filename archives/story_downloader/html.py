from archives.models import Chapter

from .html_bases import *

class HtmlMaker:
    def __init__(self, story):
        self.story = story

    def return_story(self):
        results = html_fic_base.format(
            title=self.story.fic_title,
            author=self.story.author,
            summary=self.story.summary,
            chapters=self.html_chapter()
        )

        return results

    def html_chapter(self):
        chapters = Chapter.objects.filter(
            fic=self.story.id).order_by('id')
        formatted_chapters = []
        i = 1

        if len(chapters) == 1:
            return chapters[0].content
        else:
            for chapter in chapters:
                formatted_chapters.append(
                    numbered_chapter_title.format(chapter_number=i) + chapter.content
                    )
                i += 1

            return "".join(formatted_chapters)