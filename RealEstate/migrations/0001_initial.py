# Generated by Django 5.1.6 on 2025-03-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False)),
                ('property_name', models.CharField(default='Enter Property Name', max_length=100)),
                ('property_type', models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial')], default='Residential', max_length=100)),
                ('property_price', models.IntegerField(default=0)),
                ('property_area', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Area in sqft')),
                ('property_address', models.TextField(default='Enter Address', max_length=300)),
                ('property_state', models.CharField(default='Enter State', max_length=100)),
                ('property_owner', models.CharField(max_length=100)),
                ('property_owner_contact', models.IntegerField(max_length=10)),
                ('property_owner_email', models.EmailField(max_length=100)),
                ('property_image', models.ImageField(upload_to='static/images/')),
                ('property_units', models.IntegerField(default=1)),
                ('property_furnished', models.BooleanField(default=False)),
                ('property_description', models.TextField(default='Enter Description', max_length=300)),
                ('property_status', models.CharField(choices=[('Available', 'Available'), ('Sold', 'Sold')], default='Available', max_length=100)),
            ],
        ),
    ]
