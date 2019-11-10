# Generated by Django 2.0 on 2019-11-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_delete_inputreviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='inputreviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=30)),
                ('infrastructure', models.IntegerField(default=0)),
                ('Academics', models.IntegerField(default=0)),
                ('Curricular', models.IntegerField(default=0)),
                ('Placement', models.IntegerField(default=0)),
                ('Hostel', models.IntegerField(default=0)),
                ('No_of_reviews', models.IntegerField(default=0)),
                ('Average', models.IntegerField(default=0)),
            ],
        ),
    ]
