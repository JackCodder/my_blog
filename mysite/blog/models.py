from django.db import models
from django.utils import timezone

class Post(models.Model):

    class Status(models.TextChoices): #Добавление поля статуса
        DRAFT = 'DF', 'Draft'
        PUDLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish'] # данный атрибут сообщает что сортировка будет по полю publish (убыв. порядок -)
        indexes = [
            models.Index(fields=['-publish']) #Добавление индекса базы данных
        ]

    def __str__(self):
        return self.title
