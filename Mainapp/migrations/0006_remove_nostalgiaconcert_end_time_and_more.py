# Generated by Django 4.1.7 on 2023-08-26 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0005_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nostalgiaconcert',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='nostalgiaconcert',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='nostalgiaconcert',
            name='space',
        ),
        migrations.RemoveField(
            model_name='nostalgiaconcert',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='nostalgiaconcert',
            name='ticket_available',
        ),
        migrations.RemoveField(
            model_name='nostalgiaconcert',
            name='ticket_link',
        ),
    ]
