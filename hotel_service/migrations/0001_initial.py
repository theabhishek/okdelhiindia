# Generated by Django 5.0.2 on 2025-04-12 14:37

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hotel_type', models.CharField(choices=[('budget', 'Budget'), ('mid-range', 'Mid-Range'), ('luxury', 'Luxury'), ('boutique', 'Boutique'), ('resort', 'Resort'), ('other', 'Other')], max_length=20)),
                ('address', models.TextField()),
                ('location', models.CharField(help_text='Area/Locality', max_length=200)),
                ('city', models.CharField(default='Delhi', max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('amenities', models.TextField(help_text='List of amenities provided')),
                ('check_in_time', models.TimeField(default='14:00')),
                ('check_out_time', models.TimeField(default='12:00')),
                ('affiliate_link', models.URLField(help_text='Booking affiliate link (e.g., OYO, Booking.com, etc.)')),
                ('price_range', models.CharField(help_text='Price range per night (e.g., ₹1000-₹3000)', max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Hotels',
                'ordering': ['-created_at'],
            },
        ),
    ]
