# Generated by Django 3.1.2 on 2021-02-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asyari', '0006_custumer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='custumer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
