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
    #Импорт из JSON файла старойбазы данных    
    def import_from_file():
    		with open('data.json') as data_file:    
   					data = json.load(data_file)
   					for i in data:
   						q = Tires(
   							price=data["price"],
   							model=data["model"],
   							brand=data["brand"],
   							country=data["country"],
   							tech=data["tech"],
   							size=data["size"],
   							img=data["img_big"],
   							class_tire=data["class"],
   							arch=data["type_arch"],
   							sort=data["sort_id"] )
   						if data["active"] != 1:
   							q.active = False
   						q.save()
