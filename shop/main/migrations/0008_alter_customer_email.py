# Generated by Django 4.2.5 on 2023-11-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_author_customer_task_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Электронная почта'),
        ),
    ]
