# Generated by Django 3.2.23 on 2023-12-17 19:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_user_is_verified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="avatars/"),
        ),
    ]
