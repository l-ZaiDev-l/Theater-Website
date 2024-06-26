# Generated by Django 4.1.7 on 2023-08-26 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0010_nostalgiaconcert_normal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media_Nostalgie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='nostalgie_media/')),
                ('video_url', models.URLField(blank=True, null=True)),
                ('nostalgie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mainapp.nostalgiaconcert')),
            ],
        ),
    ]
