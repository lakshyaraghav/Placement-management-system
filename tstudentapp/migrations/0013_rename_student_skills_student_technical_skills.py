# Generated by Django 3.2.6 on 2021-10-22 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tstudentapp', '0012_student_student_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_skills',
            new_name='technical_skills',
        ),
    ]