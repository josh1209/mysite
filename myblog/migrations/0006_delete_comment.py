# Generated by Django 2.1.5 on 2019-02-14 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20190213_1631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]