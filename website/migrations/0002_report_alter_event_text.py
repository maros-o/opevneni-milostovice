# Generated by Django 4.0.5 on 2022-06-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]
