# Generated by Django 3.0.4 on 2020-06-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20200608_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='owner',
        ),
        migrations.AddField(
            model_name='provider',
            name='document_status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=200, null=True),
        ),
    ]
