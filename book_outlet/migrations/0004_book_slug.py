# Generated by Django 5.0.4 on 2024-08-19 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0003_alter_book_is_bestselling"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
