# Generated by Django 5.1.3 on 2024-12-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]