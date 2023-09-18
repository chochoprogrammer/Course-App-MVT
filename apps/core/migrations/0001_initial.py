# Generated by Django 4.2.3 on 2023-09-18 00:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('short_description', models.CharField(max_length=100, verbose_name='Short Description')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('image', models.ImageField(default='peep-3.jpg', upload_to='', verbose_name='Course Image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('short_description', models.CharField(max_length=100, verbose_name='Short Description')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('image', models.ImageField(default='peep-3.jpg', upload_to='', verbose_name='Course Image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
