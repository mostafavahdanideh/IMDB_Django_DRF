# Generated by Django 4.0.4 on 2022-05-02 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_post', '0002_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]