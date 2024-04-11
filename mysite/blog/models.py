from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Добавление взаимосвязи многие-к-одному

class Post(models.Model):

    class Status(models.TextChoices): #Добавление поля статуса
        DRAFT = 'DF', 'Draft'
        PUDLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE, #поведение, которое следует применять при удалении объекта
                                related_name='blog_posts') #ь имя обратной связи, от User к Post
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices,default=Status.DRAFT)

    class Meta:
        ordering = ['-publish'] # данный атрибут сообщает что сортировка будет по полю publish (убыв. порядок -)
        indexes = [
            models.Index(fields=['-publish']) #Добавление индекса базы данных
        ]

    def __str__(self):
        return self.title
