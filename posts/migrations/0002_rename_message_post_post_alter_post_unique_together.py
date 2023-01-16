# Generated by Django 4.1.5 on 2023-01-16 13:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="message",
            new_name="post",
        ),
        migrations.AlterUniqueTogether(
            name="post",
            unique_together={("user", "post")},
        ),
    ]