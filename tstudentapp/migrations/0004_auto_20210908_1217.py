# Generated by Django 3.2.6 on 2021-09-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tstudentapp', '0003_student_student_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_achievement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_btech',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_hobbie',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_skills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
