# Generated by Django 4.1.7 on 2023-08-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0002_alter_concert_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='concerts', to='Mainapp.participant'),
        ),
    ]