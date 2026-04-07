from models import Fic, Chapter

from .utils_constants import *

class StoryDigester:
    def __init__(self, story_id):
        self.fic = Fic.objects.get(id=story_id)

    def return_title(self):
        return f"{self.fic.story_title}_par_{self.fic.author}"

    def html_fic(self):
        fic = self.fic
        results = html_fic_base.format(
            title=fic.story_title,
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