# Generated by Django 5.1.2 on 2024-10-26 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterSources', '0007_alter_sources_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='Categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='sources',
            name='description',
        ),
        migrations.CreateModel(
            name='Cat_x_Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterSources.sources')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterSources.categories')),
            ],
        ),
    ]
