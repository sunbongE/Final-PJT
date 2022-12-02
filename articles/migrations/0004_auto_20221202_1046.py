# Generated by Django 3.2.13 on 2022-12-02 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articlecomment_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecomment',
            name='hits',
        ),
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]