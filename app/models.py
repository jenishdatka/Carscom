from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Color(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/car_images')


    def __str__(self):
        return self.make

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

