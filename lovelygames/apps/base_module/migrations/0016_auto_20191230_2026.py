# Generated by Django 2.2.7 on 2019-12-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_module', '0015_auto_20191230_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
