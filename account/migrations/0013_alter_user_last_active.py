# Generated by Django 5.2 on 2025-04-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_user_last_active_alter_code_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_active',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
