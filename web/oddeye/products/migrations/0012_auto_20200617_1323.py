# Generated by Django 3.0.6 on 2020-06-17 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200617_1322'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductsEmbedding1',
            new_name='ProductsEmbedding',
        ),
        migrations.AlterModelOptions(
            name='productsembedding',
            options={'verbose_name': '상품 임베딩', 'verbose_name_plural': '상품 임베딩'},
        ),
        migrations.AlterModelTable(
            name='productsembedding',
            table='products_embedding',
        ),
    ]
