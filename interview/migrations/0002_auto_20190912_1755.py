# Generated by Django 2.2.5 on 2019-09-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='other',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='reflection',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='selection_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='selection_phase',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
