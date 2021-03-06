# Generated by Django 4.0 on 2022-03-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('product_name', models.CharField(max_length=120)),
                ('product_code', models.IntegerField(unique=True)),
                ('barcode_symbology', models.CharField(choices=[('C', 'CODE128'), ('C1', 'CODE39'), ('E', 'EAN8')], max_length=50, verbose_name='barcode_symbology')),
                ('product_cost', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('order_tax', models.IntegerField(default=0)),
                ('tax_type', models.CharField(choices=[('I', 'INCLUSIVE'), ('E', 'EXCLUSIVE')], max_length=50, verbose_name='tax_type')),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('stock_alert', models.IntegerField()),
                ('product_stock', models.IntegerField(default=0)),
                ('product_image', models.TextField()),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_discount', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
