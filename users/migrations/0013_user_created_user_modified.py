# Generated by Django 4.0.7 on 2022-10-04 22:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_company_holded_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Date time on which the object was created', verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date time on which the object was modified', verbose_name='Modified at'),
        ),
    ]