# Generated by Django 4.1.4 on 2022-12-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('BOOKED', 'Забронирован'), ('PAID', 'Оплачен'), ('PASSED', 'Пройден')], max_length=10, null=True),
        ),
    ]
