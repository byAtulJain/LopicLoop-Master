# Generated by Django 4.2.6 on 2023-10-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('headline', models.CharField(max_length=50)),
                ('difficulty', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
        ),
    ]