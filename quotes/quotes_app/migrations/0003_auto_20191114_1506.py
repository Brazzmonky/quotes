# Generated by Django 2.2.6 on 2019-11-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0002_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='user',
        ),
        migrations.AddField(
            model_name='quote',
            name='user',
            field=models.ManyToManyField(related_name='quote', to='quotes_app.User'),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]