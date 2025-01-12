# Generated by Django 5.1.3 on 2024-12-02 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_productphotos_shoesphotos_alter_shoes_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ky',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_tr',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='description_tr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='shoes_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='shoes_name_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='shoes_name_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='shoes_name_tr',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_description_tr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_name_en',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_name_ky',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_name_ru',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_name_tr',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
