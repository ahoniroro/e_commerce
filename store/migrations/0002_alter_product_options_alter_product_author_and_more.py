# Generated by Django 5.1.5 on 2025-02-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.CharField(default='admin', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
