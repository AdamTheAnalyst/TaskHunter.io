# Generated by Django 2.2.1 on 2019-05-06 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('relation', models.CharField(blank=True, max_length=255)),
                ('birthday', models.DateField()),
                ('employer', models.TextField()),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('value', models.CharField(max_length=15)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=500)),
                ('due_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('task_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskhunter.TaskType')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('type', models.CharField(choices=[('GENERAL', 'General'), ('PERSONAL', 'Personal'), ('BUSINESS', 'Business')], max_length=255)),
                ('note', models.TextField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_notes', to='taskhunter.Contact')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('type', models.CharField(choices=[('EMAIL', 'Email'), ('SLACK', 'Slack'), ('PHONE', 'Phone'), ('ADDRESS', 'Address')], max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_methods', to='taskhunter.Contact')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]