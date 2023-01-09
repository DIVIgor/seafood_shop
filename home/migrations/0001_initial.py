# Generated by Django 4.1.5 on 2023-01-09 22:38

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.StreamField([('intro', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(template='blocks/home_img.html')), ('upper_heading', wagtail.blocks.CharBlock()), ('lower_heading', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock()), ('button_text', wagtail.blocks.CharBlock()), ('button_redirection', wagtail.blocks.PageChooserBlock())], icon='home'))], blank=True, use_json_field=None)),
                ('message', wagtail.fields.StreamField([('message', wagtail.blocks.StructBlock([('upper_heading', wagtail.blocks.CharBlock()), ('lower_heading', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul']))], icon='comment'))], blank=True, use_json_field=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
