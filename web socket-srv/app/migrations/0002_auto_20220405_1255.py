# Generated by Django 3.2.12 on 2022-04-05 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='app.profile', verbose_name='recipient'),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='app.profile', verbose_name='sender'),
        ),
    ]