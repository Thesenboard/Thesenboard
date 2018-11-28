# Generated by Django 2.1.3 on 2018-11-28 13:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_visibility', models.CharField(max_length=40)),
                ('user_tags', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='These',
            fields=[
                ('thesenId', models.AutoField(primary_key=True, serialize=False)),
                ('thesenTitel', models.CharField(max_length=255)),
                ('thesenArgument', models.TextField()),
                ('thesenFazit', models.TextField()),
                ('thesenTime', models.DateTimeField(auto_now=True)),
                ('thesenQuelle', models.TextField(blank=True, null=True)),
                ('thesenUserId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThesisEntries',
            fields=[
                ('thesisEntriesId', models.AutoField(primary_key=True, serialize=False)),
                ('thesisEntriesTitel', models.CharField(max_length=255)),
                ('thesisEntriesArgument', models.TextField()),
                ('thesisEntriesFazit', models.TextField()),
                ('thesisEntriesTime', models.DateTimeField(auto_now=True)),
                ('thesisEntriesQuelle', models.TextField(blank=True, null=True)),
                ('thesisEntriesThese', models.ManyToManyField(related_name='thesisEntriesThese', to='start.These')),
                ('thesisEntriesUserId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Zwischenruf',
            fields=[
                ('zwischenrufId', models.AutoField(primary_key=True, serialize=False)),
                ('zwischenruf', models.TextField()),
                ('zwischenrufTime', models.DateTimeField(auto_now=True)),
                ('beitragsId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='start.These')),
                ('beitragsUserId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
