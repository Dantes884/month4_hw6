# Generated by Django 4.1.7 on 2023-03-02 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0003_remove_tvparser_country_genre_diroctor_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TVParser',
            new_name='KinopoiskParser',
        ),
    ]
