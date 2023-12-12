# Generated by Django 4.2.8 on 2023-12-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webSite", "0003_token"),
    ]

    operations = [
        migrations.CreateModel(
            name="Passwordresetcodes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=32)),
                ("email", models.CharField(max_length=120)),
                ("time", models.DateTimeField()),
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
