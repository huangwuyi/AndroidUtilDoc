# Generated by Django 2.0.5 on 2018-07-19 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloAndroidUtil', '0009_methodresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeTangshi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('remark', models.TextField()),
                ('oper', models.CharField(max_length=200)),
            ],
        ),
    ]
