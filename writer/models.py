from django.db import models

class Post(models.Model):
    POST_TYPES = {
        "NE": "News",
        "WR": "Writing",
        "AU": "Authorship"
    }

    type = models.CharField(
        max_length=2,
        choices=POST_TYPES,
        default="NE"
    )
    date = models.DateField()
    title = models.CharField(null=True, blank=True, max_length=200)
    body = models.TextField(max_length=6000)
    
    def __str__(self):
        return f"{self.date} : {self.body[:100]}..."