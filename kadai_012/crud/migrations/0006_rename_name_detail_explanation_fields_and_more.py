# Generated by Django 5.2.3 on 2025-06-23 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='name',
            new_name='explanation_fields',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='category',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='img',
        ),
    ]
