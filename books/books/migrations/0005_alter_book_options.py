# Generated by Django 3.2.3 on 2021-05-28 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]