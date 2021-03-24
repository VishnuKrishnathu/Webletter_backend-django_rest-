# Generated by Django 3.1.7 on 2021-03-24 14:39

from django.db import migrations, models
import webletter_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('webletter_api', '0003_posts_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogusers',
            name='profilepicture',
            field=models.ImageField(blank=True, null=True, upload_to=webletter_api.models.profilePictureUpload),
        ),
        migrations.AlterField(
            model_name='posts',
            name='theme_image',
            field=models.ImageField(blank=True, null=True, upload_to=webletter_api.models.postsPictureUpload),
        ),
    ]