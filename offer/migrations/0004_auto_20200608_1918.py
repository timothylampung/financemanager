# Generated by Django 3.0.4 on 2020-06-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_auto_20200608_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='payment_status',
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_type',
            field=models.CharField(choices=[('PRODUCT', 'PRODUCT'), ('SERVICE', 'SERVICE')], default='PRODUCT', max_length=200, null=True),
        ),
    ]