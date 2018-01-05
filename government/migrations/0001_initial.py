# Generated by Django 2.0.1 on 2018-01-05 16:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entity', '0002_auto_20180105_1600'),
        ('geography', '0006_auto_20180105_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('uid', models.CharField(blank=True, editable=False, max_length=500)),
                ('slug', models.SlugField(blank=True, help_text='Customizable slug. Defaults to Org slug without stopwords.', max_length=255)),
                ('label', models.CharField(blank=True, max_length=255)),
                ('short_label', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Bodies',
            },
        ),
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('uid', models.CharField(blank=True, editable=False, max_length=500)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='geography.Division')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='government.Jurisdiction')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('uid', models.CharField(blank=True, editable=False, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(blank=True, max_length=255)),
                ('short_label', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offices', to='government.Body')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='offices', to='geography.Division')),
                ('jurisdiction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offices', to='government.Jurisdiction')),
            ],
        ),
        migrations.AddField(
            model_name='body',
            name='jurisdiction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='government.Jurisdiction'),
        ),
        migrations.AddField(
            model_name='body',
            name='organization',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='government_body', to='entity.Organization'),
        ),
        migrations.AddField(
            model_name='body',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='government.Body'),
        ),
    ]
