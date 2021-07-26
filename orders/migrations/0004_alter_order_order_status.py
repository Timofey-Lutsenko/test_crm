# Generated by Django 3.2.5 on 2021-07-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('RGTR', 'Registered'), ('INPR', 'In Progress'), ('DONE', 'Order ready'), ('CNLD', 'Order canceled')], max_length=10),
        ),
    ]
