from django.db import models


# Create your models here.
class HuangwuyiStyle(models.Model):
    style_name = models.CharField(max_length=200)
    style_descripe = models.TextField()
    style_example = models.ImageField(upload_to='androidStyleDoc/static/androidStyleDoc/images/')


# class Soufang_ershoufang2(models.Model):
#     lsno = models.IntegerField()
#     house_source = models.CharField(max_length=50)
#     house_page = models.CharField(max_length=50)
#     house_name = models.CharField(max_length=50)
#     house_descripe = models.CharField(max_length=50)
#     house_number = models.CharField(max_length=50)
#     house_area = models.CharField(max_length=50)
#     house_height = models.CharField(max_length=50)
#     house_direction = models.CharField(max_length=50)
#     house_year = models.CharField(max_length=50)
#     house_sum_price = models.CharField(max_length=50)
#     house_per_price = models.CharField(max_length=50)
#
#     class Meta:
#         app_label = 'MSSQL'

