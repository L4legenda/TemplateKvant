# Generated by Django 3.1.4 on 2020-12-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=500, verbose_name='Комментарий')),
                ('email', models.EmailField(max_length=254, verbose_name='Введите свой email')),
            ],
        ),
    ]
