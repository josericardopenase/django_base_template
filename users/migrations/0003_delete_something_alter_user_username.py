# Generated by Django 4.0.7 on 2022-09-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_something'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Something',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]