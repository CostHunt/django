# Generated by Django 5.0.1 on 2024-03-01 15:36

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachedFile',
            fields=[
                ('id_file', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nomfichier', models.CharField(max_length=32, null=True)),
                ('path', models.CharField(max_length=32, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id_groupe', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom_groupe', models.CharField(max_length=32, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('code_role', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('libelle_role', models.CharField(max_length=32, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=32)),
                ('prenoms', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=250)),
                ('matricule', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=32)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id_message', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contenu', models.CharField(max_length=32, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('id_groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.groupe')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attacher',
            fields=[
                ('id_attacher', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('id_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.attachedfile')),
                ('id_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.message')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=32, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('id_groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.groupe')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contenir',
            fields=[
                ('id_contenir', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('id_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.attachedfile')),
                ('id_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id_comment', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contenu', models.CharField(max_length=32, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.post')),
            ],
        ),
        migrations.CreateModel(
            name='Appartenir',
            fields=[
                ('id_appartenir', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.groupe')),
                ('code_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.role')),
            ],
        ),
    ]
