# Generated by Django 3.2.13 on 2022-05-06 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_deals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.deals'),
        ),
    ]
