# Generated by Django 2.1.4 on 2018-12-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default='', max_length=50),
        ),
    ]
