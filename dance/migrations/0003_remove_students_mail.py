# Generated by Django 4.1.2 on 2022-12-09 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dance', '0002_class_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='mail',
        ),
    ]