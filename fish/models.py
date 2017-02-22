from django.db import models


class HairMaster(models.Model):
    name = models.CharField(verbose_name='название', max_length=32)
    price = models.PositiveIntegerField(verbose_name='ценв')
    category = models.ForeignKey('Category')
    image = models.ImageField(upload_to='/static/img', blank=True)
    rating = models.PositiveIntegerField(verbose_name='рейтинг', default=0)


class Category(models.Model):
    name = models.CharField(verbose_name='название', max_length=16, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='/static/img/')
    url = models.URLField(verbose_name='url', blank=True)

    def __str__(self):
        return self.name


class Locks(HairMaster):
    amount = models.PositiveIntegerField(verbose_name='количество')
    description = models.TextField(verbose_name='описание', blank=True)


class Haircut(HairMaster):
    description = models.TextField(verbose_name='описание', blank=True)


class Color(HairMaster):
    description = models.TextField(verbose_name='описание', blank=True)


class Hairdress(HairMaster):
    description = models.TextField(verbose_name='описание', blank=True)
