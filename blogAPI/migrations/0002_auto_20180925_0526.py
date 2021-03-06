# Generated by Django 2.1.1 on 2018-09-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
