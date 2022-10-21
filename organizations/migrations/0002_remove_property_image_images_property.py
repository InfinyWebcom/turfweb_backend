# Generated by Django 4.1 on 2022-10-10 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="property", name="image",),
        migrations.AddField(
            model_name="images",
            name="property",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="property_images",
                to="organizations.property",
            ),
        ),
    ]