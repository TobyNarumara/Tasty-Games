# Generated by Django 2.2.7 on 2020-01-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_module', '0022_article_torrent'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='gameplay',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
