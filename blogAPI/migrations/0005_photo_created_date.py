# Generated by Django 2.1.1 on 2018-09-18 05:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPI', '0004_auto_20180918_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
