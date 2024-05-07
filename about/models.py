from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class About(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']

    info = StreamField([
        ('info', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('upper_heading', blocks.CharBlock()),
            ('lower_heading', blocks.CharBlock()),
            ('text', blocks.RichTextBlock(
                features=['bold', 'italic', 'ol', 'ul'],
            )),
        ], icon='clipboard-list')),
    ], block_counts={'info': {'max_num': 1}}, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('info'),
    ]
