# Generated by Django 3.2.16 on 2024-07-20 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20240720_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.group'),
        ),
    ]
