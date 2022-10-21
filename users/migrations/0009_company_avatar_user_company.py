# Generated by Django 4.0.7 on 2022-10-04 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_company_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='avatar',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.company'),
            preserve_default=False,
        ),
    ]