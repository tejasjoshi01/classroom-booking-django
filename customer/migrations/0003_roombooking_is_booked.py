# Generated by Django 3.0.3 on 2020-03-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200302_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='roombooking',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
