# Generated by Django 5.0.6 on 2024-05-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0002_exit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='status',
            field=models.CharField(default='absend', max_length=20),
        ),
    ]
