# Generated by Django 3.1.4 on 2020-12-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201210_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(blank=True, choices=[('r', 'Reserved'), ('a', 'Available'), ('m', 'On maintainence')], default='a', help_text='Room availability', max_length=1),
        ),
    ]
