# Generated by Django 4.2.3 on 2023-07-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
