# Generated by Django 3.2.3 on 2021-05-26 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_itemattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
    ]
