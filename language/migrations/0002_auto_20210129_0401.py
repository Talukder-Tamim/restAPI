# Generated by Django 3.1.5 on 2021-01-29 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='framework',
        ),
        migrations.AddField(
            model_name='framework',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='language.language'),
            preserve_default=False,
        ),
    ]
