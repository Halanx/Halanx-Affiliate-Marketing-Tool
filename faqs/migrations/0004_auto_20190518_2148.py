# Generated by Django 2.2.1 on 2019-05-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0003_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]
