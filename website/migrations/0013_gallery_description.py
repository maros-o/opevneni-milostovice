# Generated by Django 4.0.5 on 2022-06-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_visitor_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(default=''),
        ),
    ]