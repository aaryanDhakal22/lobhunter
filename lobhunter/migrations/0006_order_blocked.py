# Generated by Django 5.0.6 on 2024-12-12 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobhunter', '0005_addressblocklist_phoneblocklist_delete_blocklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
