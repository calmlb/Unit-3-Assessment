# Generated by Django 3.1.3 on 2021-02-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='widget',
            old_name='age',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='widget',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='widget',
            name='name',
        ),
        migrations.AlterField(
            model_name='widget',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
