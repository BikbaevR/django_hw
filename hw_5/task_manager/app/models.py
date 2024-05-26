from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['id']

    def __str__(self):
        return self.title
