# Generated by Django 3.2.5 on 2021-07-26 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_customer_notifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customers_phone',
        ),
    ]
