# Generated by Django 5.1.1 on 2024-10-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuid', models.CharField(max_length=30)),
                ('tuname', models.CharField(max_length=30)),
                ('tuemail', models.EmailField(max_length=30)),
                ('tucontact', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
