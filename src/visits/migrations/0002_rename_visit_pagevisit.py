# Generated by Django 5.0.6 on 2024-07-02 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visit',
            new_name='PageVisit',
        ),
    ]
