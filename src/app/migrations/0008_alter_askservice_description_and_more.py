# Generated by Django 4.1 on 2022-09-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_askservice_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askservice',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quality',
            name='description',
            field=models.TextField(),
        ),
    ]