# Generated by Django 4.2.7 on 2023-11-16 20:08

import django.core.validators
from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.photos.validators.validate_max_size])),
                ('description', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_publication', models.DateTimeField(auto_now=True)),
                ('tagged_pet', models.ManyToManyField(blank=True, to='pets.pet')),
            ],
        ),
    ]