# Generated by Django 3.1.6 on 2021-02-19 20:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('cloud_architecture', models.URLField(blank=True, verbose_name='Cloud Architecture')),
                ('sre', models.URLField(blank=True, verbose_name='SRE')),
                ('pipeline', models.URLField(blank=True, verbose_name='CI/CD Pipeline')),
                ('cost_analysis', models.URLField(blank=True, verbose_name='Cost Analysis')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='theport/images/')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=True)),
                ('image', models.ImageField(default='dev/images/default.jpg', upload_to='dev/images/')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='theportapp.comment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='theportapp.project')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]