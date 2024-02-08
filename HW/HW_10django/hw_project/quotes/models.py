from django.db import models
from authors.models import Author
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
