# Generated by Django 5.0.7 on 2024-07-25 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='salary',
            new_name='income',
        ),
    ]
