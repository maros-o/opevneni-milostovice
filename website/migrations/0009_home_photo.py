# Generated by Django 4.0.5 on 2022-06-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_report_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
