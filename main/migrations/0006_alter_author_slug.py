# Generated by Django 5.1.3 on 2025-02-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_author_id_alter_category_id_alter_comment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=400, unique=True),
        ),
    ]
