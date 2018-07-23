from django.db import models

# Create your models here.
class HuangwuyiStyle(models.Model):
    style_name = models.CharField(max_length=200)
    style_descripe = models.TextField()
    style_example = models.ImageField(upload_to='androidStyleDoc/static/androidStyleDoc/images/')



