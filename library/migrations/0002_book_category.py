# Generated by Django 5.1.4 on 2025-01-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('KN', 'Kannada')], default='KN', max_length=2),
            preserve_default=False,
        ),
    ]
