# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Tires(models.Model):
    price = models.IntegerField()
    old_price = models.IntegerField()
    model = models.CharField(max_length=255)
    descript = models.TextField()
    width = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    rim = models.CharField(max_length=255)
    r_type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    instock = models.IntegerField(db_column='inStock')  # Field name made lowercase.
    tech = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    img = models.CharField(max_length=255)
    img_big = models.CharField(max_length=255)
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    active = models.IntegerField()
    slug = models.CharField(max_length=255)
    tube = models.CharField(max_length=255)
    type_arch = models.CharField(max_length=255)
    sort_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tires'
