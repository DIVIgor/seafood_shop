from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class Products(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']

    product = StreamField([
        ('product', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('upper_heading', blocks.CharBlock(required=False)),
            ('lower_heading', blocks.CharBlock()),
            ('text', blocks.TextBlock()),
        ], icon='image'))
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('product'),
    ]
