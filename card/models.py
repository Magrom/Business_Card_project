from django.db import models

from datetime import datetime, timezone


class PersonalCard(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, null=True, blank=True)
    birthday = models.DateTimeField('Год Рождения', default=datetime(year=2000, month=1, day=1, tzinfo=timezone.utc))
    photo = models.ImageField('Фото', upload_to='person/photo/%Y/%m/%d/', null=True, blank=True)
    title = models.CharField('Заголовок Сайта', max_length=50)
    title_background = models.ImageField('Фон заголовка сайта', upload_to='person/title_background/%Y/%m/%d/', null=True, blank=True)
    page_text = models.TextField('Текс страницы', )
    page_background = models.ImageField('Фон сайта', upload_to='person/page_background/%Y/%m/%d/', null=True, blank=True)
    contact_text = models.TextField('Контактные данные', max_length=1000)
    skills = models.ManyToManyField('Skills', verbose_name='Навыки')
    status = models.BooleanField('Статус', default=1)
    country = models.ForeignKey('Country', on_delete=models.DO_NOTHING, verbose_name='Страна')
    region = models.ForeignKey('Region', on_delete=models.DO_NOTHING, verbose_name='Регион')


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карточки'

class Skills(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

class Project(models.Model):
    title = models.CharField('Название пректа', max_length=100)
    description = models.TextField('Описание проекта', max_length=1000)
    personal_card = models.ForeignKey('PersonalCard', on_delete=models.CASCADE, verbose_name='Пользователь')
    images = models.ManyToManyField('ProjectImages')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Country(models.Model):
    name = models.CharField('Название страны', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class Region(models.Model):
    name = models.CharField('Название Региона', max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна', related_name='region')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

class ProjectImages(models.Model):
    images = models.ImageField('Изображеня', upload_to='project/%Y/%m/%d/')

    def __str__(self):
        return self.images.url

    class Meta:
        verbose_name = 'Изображение проекта'
        verbose_name_plural = 'Изображения проекта'
