from django.db import models

NO = {'blank': True, 'null':True}

class Categoties(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    descriptions = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='Categoties/', verbose_name='фото')

    def __str__(self):
        return f'{self.name}, {self.image}, {self.pk}, {self.descriptions}'
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    descripsions = models.TextField(verbose_name='описание', **NO)
    image = models.ImageField(upload_to='products/', **NO, verbose_name='фото')
    categories = models.ForeignKey(Categoties, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_of_creation = models.DateField(verbose_name='дата создания', **NO)
    data_last = models.DateField(verbose_name='дата создания', **NO)

    def __str__(self):
        return f'{self.name}, {self.categories}, {self.price},{self.descripsions}, {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



class Block(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    body = models.TextField(verbose_name='Содержимое')
    photo = models.ImageField(upload_to='photo/', verbose_name='Превью')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    on_published = models.BooleanField(default=True, verbose_name='статус', null=True, blank=True)
    count_view = models.IntegerField(verbose_name='соличество просмотров', default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.title}{self.body}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоговые записи'