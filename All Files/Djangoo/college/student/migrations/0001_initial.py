# Generated by Django 2.0.7 on 2018-07-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.CharField(max_length=8)),
                ('Name', models.CharField(max_length=15)),
                ('Course', models.CharField(max_length=10)),
            ],
        ),
    ]
