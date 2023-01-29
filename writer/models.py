from django.db import models

class Post(models.Model):
    date = models.DateField()
    body = models.TextField(max_length=3000)

    def __str__(self):
        return f"{self.date} : {self.body[:100]}..."