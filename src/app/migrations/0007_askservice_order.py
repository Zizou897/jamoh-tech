# Generated by Django 4.1 on 2022-09-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_askservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='askservice',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
