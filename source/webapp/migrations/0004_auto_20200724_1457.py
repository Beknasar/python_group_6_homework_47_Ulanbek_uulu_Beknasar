# Generated by Django 2.2 on 2020-07-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200724_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_deadline',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]