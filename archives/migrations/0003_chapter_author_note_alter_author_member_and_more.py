# Generated by Django 4.1.5 on 2023-01-29 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archives', '0002_fic_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='author_note',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='author',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fic',
            name='author_note',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='fic',
            name='pairing',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
