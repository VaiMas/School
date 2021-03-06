# Generated by Django 3.2.9 on 2021-11-23 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_parent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Techer_subject',
            new_name='Teacher_subject',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='techer_subject',
            new_name='teacher_subject',
        ),
        migrations.AlterField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='school.parent', verbose_name='Patent'),
        ),
    ]
