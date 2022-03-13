# Generated by Django 4.0.2 on 2022-03-13 14:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('neighbour', '0002_remove_user_moderation_status_user_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(db_index=True, max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='neighbour.user')),
            ],
            options={
                'db_table': 'sessions',
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('recipient', models.CharField(db_index=True, max_length=128)),
                ('code', models.CharField(db_index=True, max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(null=True)),
                ('attempts', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='neighbour.user')),
            ],
            options={
                'db_table': 'codes',
                'ordering': ['-created_at'],
            },
        ),
    ]