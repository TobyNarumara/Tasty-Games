# Generated by Django 2.2.7 on 2020-01-01 06:54

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_module', '0016_auto_20191230_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='release_date',
            field=models.IntegerField(),
        ),
    ]
