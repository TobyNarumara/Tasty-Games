# Generated by Django 2.2.7 on 2019-12-24 08:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base_module', '0008_auto_20191219_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='releasse_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
