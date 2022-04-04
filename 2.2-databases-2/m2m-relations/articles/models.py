from django.db import models


class Tags(models.Model):
    tag = models.CharField(max_length=70,verbose_name='Тег')

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tag = models.ManyToManyField(Tags, related_name='article', default=None)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title']

    def __str__(self):
        return self.title
