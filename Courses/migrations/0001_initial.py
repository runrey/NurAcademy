# Generated by Django 3.1.6 on 2021-04-20 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100, verbose_name='Title')),
                ('Description', models.TextField(verbose_name='Description')),
                ('Status', models.CharField(max_length=9, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20, verbose_name="User's name")),
                ('Email', models.EmailField(max_length=255, verbose_name='User email')),
                ('Password', models.CharField(max_length=30, verbose_name='User password')),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Action', models.BooleanField(verbose_name='Created / Enrolled')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='Courses',
            field=models.ManyToManyField(through='Courses.UserCourse', to='Courses.Course'),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module_title', models.CharField(max_length=100, verbose_name='Title')),
                ('Content', models.TextField(verbose_name='Content')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course')),
            ],
        ),
    ]
