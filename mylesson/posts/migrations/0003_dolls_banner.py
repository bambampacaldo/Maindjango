# Generated by Django 5.0.6 on 2024-07-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_dolls_delete_doll'),
    ]

    operations = [
        migrations.AddField(
            model_name='dolls',
            name='banner',
            field=models.ImageField(blank=True, default='bird.png', upload_to=''),
        ),
    ]
