# Generated by Django 5.0.3 on 2024-03-31 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_alter_notice_images_alter_notice_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='videos',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
