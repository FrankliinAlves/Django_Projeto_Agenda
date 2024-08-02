# Generated by Django 5.0.7 on 2024-08-02 16:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('create_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('descrition', models.TextField(blank=True)),
            ],
        ),
    ]
