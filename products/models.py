from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
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
            ('text', blocks.RichTextBlock()),
        ], icon='image'))
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('product'),
    ]
