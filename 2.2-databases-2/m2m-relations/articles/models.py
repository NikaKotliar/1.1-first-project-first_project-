from django.db import models



class Tags(models.Model):
    tag = models.CharField(max_length=70, verbose_name='Тег')

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField(Tags, through='Tags_position')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tags_position(models.Model):
    article_pos = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_info')
    tag_pos = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='tag_info')
    is_main = models.BooleanField(verbose_name='Основной тег', default=False)


