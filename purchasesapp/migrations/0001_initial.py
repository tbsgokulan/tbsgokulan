# Generated by Django 4.0 on 2022-03-24 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productapp', '0002_product_brand_product_category_product_product_unit_and_more'),
        ('settingsapp', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('additional_discount', models.IntegerField(default=0)),
                ('date', models.CharField(max_length=30)),
                ('additional_tax', models.IntegerField(default=0)),
                ('grand_total', models.BigIntegerField()),
                ('notes', models.TextField()),
                ('shipping_charges', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Ordered', 'ordered'), ('Received', 'received'), ('Pending', 'pending')], max_length=50, verbose_name='status')),
                ('paid', models.BigIntegerField(default=0)),
                ('due', models.BigIntegerField(default=0)),
                ('payment_status', models.CharField(choices=[('Paid', 'paid'), ('Partial', 'partial'), ('Unpaid', 'unpaid')], default='Unpaid', max_length=50, verbose_name='payment_status')),
                ('reference', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='productapp.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Supplier', to='people.supplier')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='settingsapp.warehouse')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='purchase_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('product_cost', models.IntegerField()),
                ('produt_stock', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
                ('product_discount', models.IntegerField()),
                ('product_tax', models.IntegerField()),
                ('sub', models.IntegerField()),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='productapp.product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Purchase', to='purchasesapp.purchase')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='payment_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update_date')),
                ('payment_date', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_reference', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_choice', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_amount', models.BigIntegerField(default=0)),
                ('payment_due', models.BigIntegerField(default=0)),
                ('payment_note', models.TextField()),
                ('payment_purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_Purchase', to='purchasesapp.purchase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]