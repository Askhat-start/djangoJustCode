from django.db import models

# Create your models here.


class Catalog(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=60)
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(verbose_name='Картинка товара', upload_to='photo/%y/%m/%d', default=None)
    description = models.TextField(verbose_name='Описание товара', default='')
    category = models.ForeignKey('Category',  verbose_name='Категория', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=60, default='')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(verbose_name='Наименование задание', max_length=60)
    completed = models.BooleanField(verbose_name='Выполнена', default=False)

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    email = models.EmailField(verbose_name='Электронная почта', default='')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)
    author_id = models.ForeignKey('Author', verbose_name='Автор', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
