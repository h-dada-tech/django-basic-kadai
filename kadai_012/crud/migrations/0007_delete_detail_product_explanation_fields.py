# Generated by Django 5.2.3 on 2025-06-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_rename_name_detail_explanation_fields_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.AddField(
            model_name='product',
            name='explanation_fields',
            field=models.TextField(blank=True, null=True),
        ),
    ]
