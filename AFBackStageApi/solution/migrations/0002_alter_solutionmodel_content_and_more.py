# Generated by Django 4.0.3 on 2022-11-22 03:45

import ckeditor_uploader.fields
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solutionmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='111'),
        ),
        migrations.AlterField(
            model_name='solutionmodel',
            name='picture',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='path/to/', variations={}, verbose_name='图片路径'),
        ),
    ]
