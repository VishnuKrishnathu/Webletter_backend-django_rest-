# Generated by Django 3.1.7 on 2021-03-25 06:01

from django.db import migrations, models
import webletter_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('webletter_api', '0004_auto_20210324_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogusers',
            name='profilepicture',
            field=models.ImageField(blank=True, default='/media/pp/default/blank.jpeg', null=True, upload_to=webletter_api.models.profilePictureUpload),
        ),
    ]
