# Generated by Django 3.1.6 on 2021-04-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='User email'),
        ),
    ]
