# Generated by Django 4.0 on 2021-12-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_ne_record_insert_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods_opt',
            name='fullname',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='foods_opt',
            name='source',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='ne_record',
            name='food_state',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='ne_record',
            name='pee_state',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='ne_record',
            name='poop_state',
            field=models.TextField(blank=True, default=''),
        ),
    ]
