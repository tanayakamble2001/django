# Generated by Django 5.0.7 on 2024-08-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('address', models.TextField(max_length=300)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]
