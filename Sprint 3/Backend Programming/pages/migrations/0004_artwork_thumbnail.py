# Generated by Django 4.0.4 on 2022-06-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_artwork_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnails/'),
        ),
    ]