# Generated by Django 4.2.6 on 2024-01-27 06:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_alter_code_language_alter_code_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='semester',
            new_name='tags',
        ),
        migrations.AddField(
            model_name='code',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
