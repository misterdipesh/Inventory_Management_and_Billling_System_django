# Generated by Django 3.1.7 on 2021-03-20 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_slug'),
        ('Customer', '0002_auto_20210319_1109'),
        ('Bill', '0003_auto_20210319_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bill_customer',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='bill_product',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='bill_quantity',
        ),
        migrations.CreateModel(
            name='TemporatyStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
        ),
        migrations.CreateModel(
            name='SoldItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_quantity', models.IntegerField(verbose_name='Quantity')),
                ('bill_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bill.bill', verbose_name='Bill NO.')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer', verbose_name='Bought By')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product', verbose_name='Product')),
            ],
        ),
    ]
