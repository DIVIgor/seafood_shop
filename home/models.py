from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class HomePage(Page):
    intro = StreamField([
        ('image', ImageChooserBlock()),
        ('upper_heading', blocks.CharBlock()),
        ('lower_heading', blocks.CharBlock()),
        ('text', blocks.RichTextBlock()),
        ('button_text', blocks.CharBlock()),
        ('button_url', blocks.URLBlock()),
    ], block_counts={
    'image': {'max_num': 1},
    'upper_heading': {'max_num': 1},
    'lower_heading': {'max_num': 1},
    'text': {'max_num': 1},
    'button_text': {'max_num': 1},
    'button_url': {'max_num': 1},
    }, blank=True)

    message = StreamField([
        ('upper_heading', blocks.CharBlock()),
        ('lower_heading', blocks.CharBlock()),
        ('text', blocks.RichTextBlock()),
    ], block_counts={
    'upper_heading': {'max_num': 1},
    'lower_heading': {'max_num': 1},
    'text': {'max_num': 1},
    }, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro'),
        StreamFieldPanel('message'),
    ]
