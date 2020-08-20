# Generated by Django 3.0.2 on 2020-08-17 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('-2', 'Ужасно'), ('-1', 'Плохо'), ('0', 'Нормально'), ('1', 'Хорошо'), ('2', 'Отлично')], db_index=True, max_length=5, verbose_name='Общая оценка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('publish', models.DateTimeField(verbose_name='Дата')),
                ('status', models.CharField(choices=[('да', 'Да'), ('нет', 'Нет')], default='Да', max_length=5, verbose_name='Общий чат')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Облако тэгов')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
