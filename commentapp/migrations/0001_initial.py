# Generated by Django 3.2.5 on 2021-08-05 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articleapp', '0002_auto_20210805_1609'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='articleapp.article')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
