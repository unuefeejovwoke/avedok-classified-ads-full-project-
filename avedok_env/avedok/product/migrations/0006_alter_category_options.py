# Generated by Django 4.0.3 on 2022-03-09 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
