# Generated by Django 5.1.6 on 2025-03-08 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pd', '0003_rename_id_productcategory_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='category_id',
        ),
    ]
