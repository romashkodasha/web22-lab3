# Generated by Django 4.1.2 on 2022-10-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dance', '0002_alter_timetable_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='timetable',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Timetable',
        ),
    ]