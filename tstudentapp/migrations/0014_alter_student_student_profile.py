# Generated by Django 3.2.6 on 2021-10-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tstudentapp', '0013_rename_student_skills_student_technical_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_profile',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
