# Generated by Django 5.0.6 on 2024-06-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0003_alter_sitesetup_options_menulink_site_setup'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='favicoin',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m'),
        ),
    ]
