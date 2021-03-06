# Generated by Django 4.0.3 on 2022-04-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='question_text',
        ),
        migrations.AddField(
            model_name='user',
            name='user_connect',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_question',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
