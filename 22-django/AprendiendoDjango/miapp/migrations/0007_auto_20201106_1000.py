# Generated by Django 3.1.2 on 2020-11-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0006_choice_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=250),
        ),
    ]
