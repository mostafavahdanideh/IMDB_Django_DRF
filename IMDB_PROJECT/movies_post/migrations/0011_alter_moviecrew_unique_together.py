# Generated by Django 4.0.4 on 2022-05-02 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_post', '0010_alter_moviecast_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='moviecrew',
            unique_together={('person_name', 'movie', 'job')},
        ),
    ]