# Generated by Django 3.0.5 on 2020-06-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200630_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='/static/images/default_blog_image.png', upload_to='static/images/'),
        ),
    ]
