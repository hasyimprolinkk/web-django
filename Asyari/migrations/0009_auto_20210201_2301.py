# Generated by Django 3.1.2 on 2021-02-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asyari', '0008_auto_20210201_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='no_image.jpg', null=True, upload_to=''),
        ),
    ]
