# Generated by Django 3.1.2 on 2020-12-06 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asyari', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='custumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asyari.custumer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asyari.product'),
        ),
    ]
