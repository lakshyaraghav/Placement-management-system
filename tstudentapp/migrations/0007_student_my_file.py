# Generated by Django 3.2.6 on 2021-09-11 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tstudentapp', '0006_auto_20210909_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='my_file',
            field=models.FileField(blank=True, upload_to='tstudentapp/doc'),
        ),
    ]
