# Generated by Django 4.0 on 2021-12-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_ne_record_food_state_ne_record_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pee_opt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Foods',
            new_name='Foods_opt',
        ),
        migrations.AddField(
            model_name='ne_record',
            name='pee_cap',
            field=models.IntegerField(default=0),
        ),
    ]