# Generated by Django 3.2.6 on 2021-08-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CallBoard', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
    ]
