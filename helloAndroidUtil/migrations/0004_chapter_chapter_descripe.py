# Generated by Django 2.0.5 on 2018-07-16 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloAndroidUtil', '0003_methonparameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_descripe',
            field=models.CharField(default='defaultdescripe', max_length=2000),
            preserve_default=False,
        ),
    ]
