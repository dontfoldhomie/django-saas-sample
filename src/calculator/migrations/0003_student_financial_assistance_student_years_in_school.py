# Generated by Django 5.0.7 on 2024-07-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_student_yearly_tuition'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='financial_assistance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='years_in_school',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
