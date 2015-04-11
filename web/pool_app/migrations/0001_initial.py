# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PoolTagAnswer',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('option_selected', models.CharField(max_length=10)),
                ('option_text', models.TextField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('pool_tag_answered', models.DateTimeField()),
            ],
            options={
                'db_table': 'pool_tag_answer',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PoolTagMaster',
            fields=[
                ('pool_id', models.IntegerField(unique=True)),
                ('pool_tag', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('question', models.TextField()),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('pool_start', models.DateTimeField()),
                ('pool_end', models.DateTimeField()),
                ('pool_tag_created', models.DateTimeField()),
                ('option1_count', models.IntegerField()),
                ('option2_count', models.IntegerField()),
                ('option3_count', models.IntegerField()),
                ('option4_count', models.IntegerField()),
            ],
            options={
                'db_table': 'pool_tag_master',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PoolUsers',
            fields=[
                ('id', models.IntegerField(unique=True)),
                ('user_id', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20, blank=True)),
                ('location', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'db_table': 'pool_users',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
