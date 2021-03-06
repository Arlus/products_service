# Generated by Django 2.0.13 on 2019-03-22 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190319_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='replacement_product',
            field=models.OneToOneField(blank=True, help_text='The replacement_product is the new, which replaces the old replaced_product.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replaced_product', to='products.Product'),
        ),
    ]
