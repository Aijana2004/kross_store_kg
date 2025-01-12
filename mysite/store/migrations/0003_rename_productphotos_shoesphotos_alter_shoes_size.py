# Generated by Django 5.1.3 on 2024-12-02 15:31

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_shoes_size'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductPhotos',
            new_name='ShoesPhotos',
        ),
        migrations.AlterField(
            model_name='shoes',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61)], max_length=100),
        ),
    ]
