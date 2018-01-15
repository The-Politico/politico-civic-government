# Generated by Django 2.0.1 on 2018-01-15 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='organization',
            field=models.OneToOneField(blank=True, help_text='All parties except Independent should attach to an Org.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='political_party', to='entity.Organization'),
        ),
    ]