# Generated by Django 5.1.3 on 2024-12-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_band_like_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
