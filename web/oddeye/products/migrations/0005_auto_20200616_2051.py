# Generated by Django 3.0.6 on 2020-06-16 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200616_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsembedding2',
            name='product_ID',
        ),
        migrations.DeleteModel(
            name='ProductsEmbedding1',
        ),
        migrations.DeleteModel(
            name='ProductsEmbedding2',
        ),
    ]
