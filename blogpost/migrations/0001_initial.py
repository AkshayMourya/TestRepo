# Generated by Django 2.1.1 on 2018-09-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=30)),
                ('created_at', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'blog_details_table',
            },
        ),
    ]
