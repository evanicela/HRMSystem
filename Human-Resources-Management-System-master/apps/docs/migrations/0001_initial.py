# Generated by Django 4.1.5 on 2023-02-06 15:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0007_alter_employee_snils_number'),
        ('corecode', '0008_documenttype_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocBulkUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('csv_file', models.FileField(upload_to='docs/bulkupload/')),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('active', 'Действующий'), ('inactive', 'Архив')], default='active', max_length=10, verbose_name='Статус')),
                ('serial', models.CharField(max_length=200, unique=True, verbose_name='Серия')),
                ('number', models.CharField(max_length=200, verbose_name='Номер №')),
                ('date_of_issue', models.DateField(default=django.utils.timezone.now, verbose_name='Дата выдачи, С')),
                ('date_of_expiry', models.DateField(default=django.utils.timezone.now, verbose_name='Дата окончание, ДО')),
                ('issued_authority', models.CharField(max_length=200, verbose_name='Кем выдан')),
                ('address', models.TextField(blank=True, verbose_name='Адрес в РФ')),
                ('others', models.TextField(blank=True, verbose_name='Другие')),
                ('scanned_doc', models.FileField(blank=True, upload_to='docs/uploads/', verbose_name='Загрузить файл')),
                ('citizenship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.citizenship', verbose_name='Гражданство')),
                ('doc_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.documenttype', verbose_name='Тип документа')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee', verbose_name='Сотрудник')),
            ],
            options={
                'ordering': ['current_status'],
            },
        ),
    ]
