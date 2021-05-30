# Generated by Django 3.2.3 on 2021-05-26 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20210526_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size')),
            ],
        ),
    ]