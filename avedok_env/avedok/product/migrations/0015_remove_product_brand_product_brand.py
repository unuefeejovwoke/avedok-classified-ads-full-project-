# Generated by Django 4.0.3 on 2022-04-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_rename_brand_name_brand_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ManyToManyField(blank=True, to='product.brand'),
        ),
    ]
