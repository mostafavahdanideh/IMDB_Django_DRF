# Generated by Django 4.0.4 on 2022-05-02 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_post', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MovieCast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies_post.movie')),
                ('person_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies_post.person')),
            ],
            options={
                'verbose_name_plural': 'MoviesCast',
            },
        ),
    ]