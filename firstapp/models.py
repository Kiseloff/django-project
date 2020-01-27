from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Интернет адрес пиццерии')

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название пиццы')
    short_description = models.TextField(verbose_name='Краткое описание')
    price = models.IntegerField(default=0, verbose_name='Цена')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name