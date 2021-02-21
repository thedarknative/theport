# Generated by Django 3.1.6 on 2021-02-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theportapp', '0004_remove_comment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]