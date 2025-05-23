# Generated by Django 5.1.7 on 2025-04-06 16:01

import account.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_user_google_id_remove_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('expired_data', models.DateTimeField(default=account.models.time_default)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
