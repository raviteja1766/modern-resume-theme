# Generated by Django 3.0.4 on 2020-03-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]