# Generated by Django 4.0.1 on 2023-02-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketingform',
            old_name='done_by_status',
            new_name='done_by',
        ),
        migrations.AddField(
            model_name='marketingform',
            name='status',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]