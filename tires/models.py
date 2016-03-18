 # -*- coding: utf-8 -*-

from django.db import models
import json

# --- Каталог шин ---
class Tires(models.Model):
    #Цена шины
    price = models.IntegerField()

    #Модель шины
    model = models.CharField(max_length=200)

    #Производитель
    brand = models.CharField(max_length=50)

    #Страна изготовления
    country = models.CharField(max_length=30)

    #Нагрузка
    tech = models.CharField(max_length=100)

    #Типоразмер
    size = models.CharField(max_length=100)

    #Путь до миниатюры
    img = models.CharField(max_length=100)

    #Назначение шины
    class_tire = models.CharField(max_length=100)

    #Активность позиции
    active = models.BooleanField(default=True)

    #Тип шины (архитектура)
    arch = models.CharField(max_length=20)

    #Сортировка
    sort = models.IntegerField(default=0)

    #Дата изменения
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        text = self.size + " " + self.brand + " " + self.model
        return text
