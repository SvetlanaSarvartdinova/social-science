# Generated by Django 3.1.2 on 2020-12-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20201120_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firquiz',
            name='answerText',
            field=models.CharField(max_length=100, verbose_name='Правильный вариант'),
        ),
        migrations.AlterField(
            model_name='firquiz',
            name='topic',
            field=models.CharField(choices=[('soc', 'Типы обществ'), ('tax', 'Налоги'), ('fam', 'Семья'), ('state', 'Государство')], max_length=100, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='secquiz',
            name='answerText',
            field=models.CharField(max_length=100, verbose_name='Правильный вариант'),
        ),
        migrations.AlterField(
            model_name='secquiz',
            name='option1',
            field=models.CharField(max_length=100, verbose_name='Вариант 1'),
        ),
        migrations.AlterField(
            model_name='secquiz',
            name='option2',
            field=models.CharField(max_length=100, verbose_name='Вариант 2'),
        ),
        migrations.AlterField(
            model_name='secquiz',
            name='option3',
            field=models.CharField(max_length=100, verbose_name='Вариант 3'),
        ),
        migrations.AlterField(
            model_name='secquiz',
            name='option4',
            field=models.CharField(max_length=100, verbose_name='Вариант 4'),
        ),
        migrations.AlterField(
            model_name='secquiz',
            name='topic',
            field=models.CharField(choices=[('soc', 'Типы обществ'), ('tax', 'Налоги'), ('fam', 'Семья'), ('state', 'Государство')], max_length=100, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='thdquiz',
            name='answerText',
            field=models.CharField(max_length=100, verbose_name='Правильный вариант'),
        ),
        migrations.AlterField(
            model_name='thdquiz',
            name='option1',
            field=models.CharField(max_length=100, verbose_name='Вариант 1'),
        ),
        migrations.AlterField(
            model_name='thdquiz',
            name='option2',
            field=models.CharField(max_length=100, verbose_name='Вариант 2'),
        ),
        migrations.AlterField(
            model_name='thdquiz',
            name='topic',
            field=models.CharField(choices=[('soc', 'Типы обществ'), ('tax', 'Налоги'), ('fam', 'Семья'), ('state', 'Государство')], max_length=100, verbose_name='Тема'),
        ),
    ]