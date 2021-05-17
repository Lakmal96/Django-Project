# Generated by Django 3.2 on 2021-05-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_auto_20210515_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]