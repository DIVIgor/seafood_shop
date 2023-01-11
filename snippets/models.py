from django.db import models

from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet
from wagtail import blocks


@register_snippet
class BackgroundImage(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]

    def __str__(self):
        return 'background image'


@register_snippet
class Header(models.Model):
    upper_header = models.CharField(max_length=255, blank=True)
    lower_header = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('upper_header'),
        FieldPanel('lower_header'),
    ]

    def __str__(self):
        return self.upper_header


@register_snippet
class NavbarTitle(models.Model):
    title = models.CharField(max_length=255, blank=True)
    url = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        PageChooserPanel('url'),
    ]

    def __str__(self):
        return self.title


@register_snippet
class Footer(models.Model):
    content = models.CharField(max_length=255)

    panels = [
        FieldPanel('content'),
    ]

    def __str__(self):
        return self.content
