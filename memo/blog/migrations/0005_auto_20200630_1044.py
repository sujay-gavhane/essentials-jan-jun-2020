# Generated by Django 3.0.5 on 2020-06-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='/static/images/default_blog_image.png', upload_to='images/'),
        ),
    ]