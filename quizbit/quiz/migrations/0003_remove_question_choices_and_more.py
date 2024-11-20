# Generated by Django 5.1.3 on 2024-11-20 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_practicehistory_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.CreateModel(
            name='AnswerChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='correct_answer_question', to='quiz.answerchoice'),
        ),
    ]
