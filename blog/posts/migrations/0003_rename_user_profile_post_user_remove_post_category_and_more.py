# Generated by Django 4.2.6 on 2023-11-07 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_userprofile_options_alter_userprofile_managers_and_more"),
        ("posts", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="user_profile",
            new_name="user",
        ),
        migrations.RemoveField(
            model_name="post",
            name="category",
        ),
        migrations.AddField(
            model_name="post",
            name="category_name",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.category",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(null=True),
        ),
    ]