# Generated by Django 2.2.7 on 2019-11-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default='C:\\Users\\Настя\\Desktop\\Fullstack_SF\\modul_23_D6\\library\\media/blank-book-cover.png', upload_to='book-cover/'),
        ),
    ]
