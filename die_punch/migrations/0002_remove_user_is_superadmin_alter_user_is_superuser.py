# Generated by Django 4.0.1 on 2023-02-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('die_punch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superadmin',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
