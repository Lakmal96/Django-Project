# Generated by Django 3.2 on 2021-05-19 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catogories', '0002_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='catogories/'),
        ),
    ]
