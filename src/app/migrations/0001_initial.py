# Generated by Django 4.1 on 2022-08-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='img_banner')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('libele', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
            },
        ),
    ]
