# Generated by Django 4.2.3 on 2023-07-30 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_topic_files'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-created']},
        ),
    ]
