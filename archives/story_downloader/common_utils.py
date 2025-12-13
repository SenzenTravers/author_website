numbered_chapter_title = """<h2 style="margin-top: 4em;margin-bottom:2em;text-align: center; text-transform: uppercase">{chapter_name}</h2>"""


def return_chapter_title(chapter, chapter_index):
    if chapter.chapter_title:
        return f"Chapitre {chapter_index} : {chapter.chapter_title}"
    else:
        return f"Chapitre {chapter_index}"


def return_html_chapter_title(chapter, chapter_index):
    chapter_name = return_chapter_title(chapter, chapter_index)
    return numbered_chapter_title.format(chapter_name=chapter_name)
