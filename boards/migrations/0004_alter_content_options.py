# Generated by Django 3.2.15 on 2022-08-04 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_board_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ('is_completed', 'created_at')},
        ),
    ]
