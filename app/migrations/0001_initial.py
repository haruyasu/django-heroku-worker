# Generated by Django 3.2.11 on 2022-01-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(default=None, max_length=255)),
                ('url', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]
