from django.db import models


# Create your models here.

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=200)
    chapter_lsno = models.IntegerField()
    def __str__(self):
        return str(self.chapter_lsno) + " - " + str(self.chapter_name)


class ChapterItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_descripe = models.CharField(max_length=2000)
    item_lsno = models.IntegerField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_lsno) + " - " + str(self.item_name)


class ItemMethod(models.Model):
    method_name = models.CharField(max_length=200)
    method_descripe = models.CharField(max_length=2000)
    method_lsno = models.IntegerField()
    chapter_item = models.ForeignKey(ChapterItem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.method_lsno) + " - " + str(self.method_name)
