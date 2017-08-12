from django.db import models


class HairMaster(models.Model):
    name = models.CharField(verbose_name='название', max_length=32)
    price = models.PositiveIntegerField(verbose_name='цена')
    category = models.ForeignKey('Category')
    image = models.ImageField(upload_to='static/img', blank=True)
    rating = models.PositiveIntegerField(verbose_name='рейтинг', default=0)

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='название', max_length=16, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='static/img')
    url = models.URLField(verbose_name='url', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Locks(HairMaster):
    amount = models.PositiveIntegerField(verbose_name='количество')
    description = models.TextField(verbose_name='описание', blank=True)

    class Meta:
        verbose_name = 'Плетения'
        verbose_name_plural = 'Плетения'


class Haircut(HairMaster):
    description = models.TextField(verbose_name='описание', blank=True)

    class Meta:
        verbose_name = 'Стрижка'
        verbose_name_plural = 'Стрижки'


class Color(HairMaster):
    description = models.TextField(verbose_name='описание', blank=True)

    class Meta:
        verbose_name = 'Окрашивание'
        verbose_name_plural = 'Окрашивания'

class Hairdress(HairMaster):
    description = models.TextField(verbose_name='описание', blank=True)

    class Meta:
        verbose_name = 'Прическа'
        verbose_name_plural = 'Прически'