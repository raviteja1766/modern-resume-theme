# Generated by Django 3.0.4 on 2020-03-18 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0003_remove_cast_is_debut_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='imdb.Director'),
        ),
    ]
