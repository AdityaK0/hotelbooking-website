# Generated by Django 4.1.2 on 2023-03-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0002_vendorregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorregister',
            name='vendor_DOB',
            field=models.DateField(default=None),
        ),
    ]