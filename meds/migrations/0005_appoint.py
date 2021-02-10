# Generated by Django 3.1.3 on 2021-02-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0004_auto_20210206_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.TextField()),
                ('date', models.TextField()),
                ('department', models.TextField()),
                ('doctor', models.TextField()),
                ('mess', models.TextField()),
            ],
        ),
    ]