# Generated by Django 4.0.7 on 2022-10-04 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
