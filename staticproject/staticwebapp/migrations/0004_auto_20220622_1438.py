# Generated by Django 3.2.13 on 2022-06-22 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticwebapp', '0003_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='name1',
        ),
    ]
