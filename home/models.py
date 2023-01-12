from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class HomePage(Page):
    max_count = 1

    intro = StreamField([
        ('intro', blocks.StructBlock([
            ('image', ImageChooserBlock(template='blocks/home_img.html',)),
            ('upper_heading', blocks.CharBlock()),
            ('lower_heading', blocks.CharBlock()),
            ('text', blocks.TextBlock()),
            ('button_text', blocks.CharBlock(required=False)),
            ('button_redirection', blocks.PageChooserBlock(required=False)),
        ], icon='home')),
    ], block_counts={
        'intro': {'max_num': 1},
    }, blank=True)

    message = StreamField([
        ('message', blocks.StructBlock([
            ('upper_heading', blocks.CharBlock()),
            ('lower_heading', blocks.CharBlock()),
            ('text', blocks.RichTextBlock(
                features=[
                    'bold', 'italic', 'ol', 'ul'
                ]
            )),
        ], icon='comment'))
    ], block_counts={
    'message': {'max_num': 1},
    }, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro'),
        StreamFieldPanel('message'),
    ]
