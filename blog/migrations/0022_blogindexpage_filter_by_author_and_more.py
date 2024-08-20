# Generated by Django 5.0.6 on 2024-07-04 10:09

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0021_blogentrypage_header_cta_buttons_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogindexpage",
            name="filter_by_author",
            field=models.BooleanField(default=False, verbose_name="Filter by author"),
        ),
        migrations.AddField(
            model_name="blogindexpage",
            name="filter_by_category",
            field=models.BooleanField(default=True, verbose_name="Filter by category"),
        ),
        migrations.AddField(
            model_name="blogindexpage",
            name="filter_by_source",
            field=models.BooleanField(
                default=False,
                help_text="The source is the organization of the post author",
                verbose_name="Filter by source",
            ),
        ),
        migrations.AddField(
            model_name="blogindexpage",
            name="filter_by_tag",
            field=models.BooleanField(default=True, verbose_name="Filter by tag"),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="Displayed on the top of the category page",
                max_length=500,
                verbose_name="Description",
            ),
        ),
    ]