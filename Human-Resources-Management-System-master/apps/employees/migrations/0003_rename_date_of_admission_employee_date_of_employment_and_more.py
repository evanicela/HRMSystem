# Generated by Django 4.1.5 on 2023-02-04 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0005_documentcategory'),
        ('employees', '0002_alter_employee_passport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='date_of_admission',
            new_name='date_of_employment',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='parent_mobile_number',
            new_name='mobile_number',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='registration_number',
            new_name='personnel_number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='current_class',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='passport',
        ),
        migrations.AddField(
            model_name='employee',
            name='current_doc_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.documentcategory'),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='employees/photos/', verbose_name='Фото'),
        ),
    ]
