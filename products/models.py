from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class Products(Page):
    product = StreamField([
        ('image', ImageChooserBlock()),
        ('upper_heading', blocks.CharBlock()),
        ('lower_heading', blocks.CharBlock()),
        ('text', blocks.RichTextBlock()),
    ], block_counts={
    'image': {'max_num': 1},
    'upper_heading': {'max_num': 1},
    'lower_heading': {'max_num': 1},
    'text': {'max_num': 1},
    }, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('product'),
    ]
