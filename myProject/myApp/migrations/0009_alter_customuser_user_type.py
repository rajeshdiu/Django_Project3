# Generated by Django 4.2.6 on 2023-10-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0008_teachermodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[(1, "admin"), (2, "Teacher"), (3, "students")],
                default=1,
                max_length=50,
            ),
        ),
    ]