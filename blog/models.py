from django.db import models
from datetime import datetime, timedelta


class Author(models.Model):
    name = models.CharField(max_length=60)
    bio = models.TextField()

    def __str__(self):
        return f'Author: {self.name}'

class Post(models.Model):
    title = models.CharField(max_length=31)
    content = models.TextField()
    published_date = models.DateTimeField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def published_recently(self):
        now = datetime.now()
        return (True if now - timedelta(days=7) <= self.published_date else False)

    def __str__(self):
        return f'Post: {self.title}'