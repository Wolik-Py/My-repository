# Generated by Django 3.1.7 on 2021-03-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(default=4545, verbose_name='Текст комментария'),
            preserve_default=False,
        ),
    ]
