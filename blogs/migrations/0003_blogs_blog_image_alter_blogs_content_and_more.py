# Generated by Django 4.2.3 on 2023-08-13 02:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_popular_blogs_blogs_delete_regular_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='blog_image',
            field=models.FileField(default=None, max_length=500, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.TextField(),
        ),
    ]
