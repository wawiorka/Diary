# Generated by Django 5.2.1 on 2025-05-26 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user',
            new_name='author',
        ),
    ]
