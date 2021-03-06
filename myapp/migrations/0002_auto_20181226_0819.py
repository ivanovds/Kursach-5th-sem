# Generated by Django 2.1.4 on 2018-12-26 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='order',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Course'),
        ),
    ]
