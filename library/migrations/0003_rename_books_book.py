# Generated by Django 4.0.2 on 2022-04-01 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_books'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
