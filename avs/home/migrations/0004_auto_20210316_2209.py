# Generated by Django 3.1.5 on 2021-03-16 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210316_2039'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crendials',
            new_name='Credentials',
        ),
        migrations.RenameField(
            model_name='credentials',
            old_name='Crendial_image',
            new_name='Credential_image',
        ),
        migrations.RenameField(
            model_name='credentials',
            old_name='Crendial_name',
            new_name='Credential_name',
        ),
    ]
