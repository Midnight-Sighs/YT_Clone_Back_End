# Generated by Django 3.2.8 on 2021-10-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeclone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='comments',
            name='videoId',
            field=models.TextField(max_length=11),
        ),
        migrations.AlterField(
            model_name='replies',
            name='content',
            field=models.TextField(max_length=250),
        ),
    ]
