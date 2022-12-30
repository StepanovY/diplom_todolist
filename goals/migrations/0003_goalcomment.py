# Generated by Django 4.1.3 on 2022-12-29 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0002_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('text', models.TextField(verbose_name='Текст')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goal_comment', to='goals.goal', verbose_name='Цель')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goal_comment', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий к цели',
                'verbose_name_plural': 'Комментарии к цели',
            },
        ),
    ]
