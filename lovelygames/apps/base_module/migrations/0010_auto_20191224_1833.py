# Generated by Django 2.2.7 on 2019-12-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_module', '0009_article_releasse_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='releasse_date',
            field=models.DateField(),
        ),
    ]