# Generated by Django 5.2 on 2025-04-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1212, upload_to='profile_images'),
            preserve_default=False,
        ),
    ]
