# Generated by Django 4.0.5 on 2022-06-14 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_galery_alter_home_photo_id_galery_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Home_photo',
            new_name='Home_image',
        ),
        migrations.RenameModel(
            old_name='Galery',
            new_name='Gallery',
        ),
        migrations.DeleteModel(
            name='Galery_photo',
        ),
        migrations.AddField(
            model_name='gallery_image',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.gallery'),
        ),
    ]
