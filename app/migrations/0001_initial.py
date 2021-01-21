# Generated by Django 3.1.5 on 2021-01-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='شناسه')),
                ('pid', models.CharField(max_length=100, verbose_name='زیر شاخه')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('title', models.CharField(max_length=100, verbose_name='تیتر')),
                ('image', models.ImageField(upload_to='image', verbose_name='تصویر')),
                ('content', models.TextField(max_length=500, verbose_name='مشخصات')),
                ('tag', models.CharField(max_length=200, verbose_name='برچسب')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
