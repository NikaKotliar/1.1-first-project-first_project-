from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exists}, {self.slug}'

