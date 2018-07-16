from django.db import models


# Create your models here.

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=200)
    chapter_lsno = models.IntegerField()
    chapter_descripe = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.chapter_lsno) + " - " + str(self.chapter_name) + " - " + str(self.chapter_descripe)


class ChapterItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_descripe = models.CharField(max_length=2000)
    item_lsno = models.IntegerField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_lsno) + " - " + str(self.item_name)+ " - " + str(self.item_descripe)


class ItemMethod(models.Model):
    method_name = models.CharField(max_length=200)
    method_descripe = models.CharField(max_length=2000)
    method_lsno = models.IntegerField()
    method_type = models.CharField(max_length=50)
    chapter_item = models.ForeignKey(ChapterItem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.method_lsno) + " - " + str(self.method_type) + " - " + str(self.method_name) + " - " + str(self.method_descripe)


class MethodParameter(models.Model):
    parameter_lsno = models.IntegerField()
    parameter_type = models.CharField(max_length=200)
    parameter_name = models.CharField(max_length=200)
    parameter_descripe = models.CharField(max_length=1000)
    itemMethod = models.ForeignKey(ItemMethod, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.parameter_lsno) + " - " + str(self.parameter_type) + " - " + str(self.parameter_name) + " - " + str(self.parameter_descripe)
