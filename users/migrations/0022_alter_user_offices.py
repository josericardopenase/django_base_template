# Generated by Django 4.0.8 on 2022-10-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('users', '0021_user_offices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='offices',
            field=models.ManyToManyField(related_name='offices', to='companies.company'),
        ),
    ]