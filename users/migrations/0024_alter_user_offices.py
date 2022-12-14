# Generated by Django 4.0.8 on 2022-10-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0003_office_extra_field'),
        ('users', '0023_alter_user_offices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='offices',
            field=models.ManyToManyField(related_name='employees', to='offices.office'),
        ),
    ]
