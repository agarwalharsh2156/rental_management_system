# Generated by Django 5.1.6 on 2025-03-03 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate', '0006_rename_agreement_description_lease_agreement_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property_unit',
            old_name='price',
            new_name='rent',
        ),
    ]
