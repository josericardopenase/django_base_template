# Generated by Django 4.0.8 on 2022-10-11 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('users', '0020_alter_user_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='offices',
            field=models.ManyToManyField(to='companies.company'),
        ),
    ]