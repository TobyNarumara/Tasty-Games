# Generated by Django 2.2.7 on 2019-12-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_module', '0013_auto_20191230_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
