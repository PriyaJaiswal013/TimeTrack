# Generated by Django 3.2 on 2021-04-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210422_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertasks',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Task Names'},
        ),
        migrations.AlterField(
            model_name='usertasks',
            name='end_time',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
