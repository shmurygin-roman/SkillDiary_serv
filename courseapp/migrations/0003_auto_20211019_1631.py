# Generated by Django 3.2 on 2021-10-19 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseapp', '0002_remove_profession_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addinfo', to='courseapp.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='courseapp.profession'),
        ),
    ]
