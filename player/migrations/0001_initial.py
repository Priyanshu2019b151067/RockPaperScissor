# Generated by Django 4.0.1 on 2022-01-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('playname', models.CharField(max_length=60)),
            ],
        ),
    ]
