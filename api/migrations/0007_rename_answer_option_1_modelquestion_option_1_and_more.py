# Generated by Django 4.0.1 on 2022-10-30 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_question_text_modelquestion_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelquestion',
            old_name='answer_option_1',
            new_name='option_1',
        ),
        migrations.RenameField(
            model_name='modelquestion',
            old_name='answer_option_2',
            new_name='option_2',
        ),
        migrations.RenameField(
            model_name='modelquestion',
            old_name='answer_option_3',
            new_name='option_3',
        ),
        migrations.RenameField(
            model_name='modelquestion',
            old_name='answer_option_4',
            new_name='option_4',
        ),
    ]
