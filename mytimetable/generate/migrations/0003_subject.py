# Generated by Django 4.2 on 2023-06-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate', '0002_rename_num_of_activities_totalactivities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hours', models.IntegerField()),
            ],
        ),
    ]
