from django.db import models


# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    creations_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['id']

    def __str__(self):
        return f"{self.name}"