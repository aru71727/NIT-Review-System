# Generated by Django 2.0 on 2019-11-10 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_inputreviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]