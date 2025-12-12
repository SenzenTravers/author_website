class EpubMaker:
    def __init__(
        self, fic, starting_url
    ):
        self.fic = fic
        self.starting_url = starting_url

    def html_fic(self):
        fic = self.fic
        results = html_fic_base.format(
            title=fic.fic_title,
            author=fic.author,
            summary=fic.summary,
            chapters=self.html_chapter()
        )

        return results