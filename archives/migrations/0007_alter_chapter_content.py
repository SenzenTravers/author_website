# Generated by Django 4.1.5 on 2023-02-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0006_alter_chapter_content_alter_fic_author_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=models.TextField(max_length=1000000),
        ),
    ]
