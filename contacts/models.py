from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import StreamFieldPanel
from wagtail import blocks

from django.core.validators import RegexValidator


class Contacts(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']

    contact_info = StreamField([
        ('info', blocks.StreamBlock(
            [
                ('headers', blocks.StructBlock([
                    ('upper_heading', blocks.CharBlock()),
                    ('lower_heading', blocks.CharBlock()),
                ], icon='title')),
                ('schedule', blocks.StreamBlock([
                    ('string', blocks.StructBlock([
                        ('day', blocks.ChoiceBlock(choices=[
                            ('Sunday', 'Sunday'),
                            ('Monday', 'Monday'),
                            ('Tuesday', 'Tuesday'),
                            ('Wednesday', 'Wednesday'),
                            ('Thursday', 'Thursday'),
                            ('Friday', 'Friday'),
                            ('Saturday', 'Saturday'),
                        ])),
                        ('worktime_from', blocks.TimeBlock(required=False)),
                        ('worktime_to', blocks.TimeBlock(required=False)),
                    ], icon='list-ul'))
                ], required=False, block_counts={
                    'string': {'min_num': 7, 'max_num': 7},
                }, icon='date')),
                ('address', blocks.StructBlock([
                    ('address_upper', blocks.CharBlock(max_length=250)),
                    ('address_lower', blocks.CharBlock(
                        required=False, max_length=250,
                    )),
                ], icon='home')),
                ('contacts', blocks.StructBlock([
                    ('short_message', blocks.CharBlock(
                        required=False, max_length=250,
                    )),
                    ('phone', blocks.CharBlock(
                        required=False, min_length=10, max_length=13,
                        validators=[RegexValidator(
                            regex=r'\d{10,13}$',
                            message='Please, enter digits only.'
                        ),],
                        help_text='Please, enter a number from 10 to 13 digits length.'
                    )),
                    ('email', blocks.EmailBlock(
                        required=False, max_length=250,
                    )),
                ], icon='mail'))
            ], icon='clipboard-list', block_counts={
                'headers': {'max_num': 1},
                'schedule': {'max_num': 1},
                'address': {'max_num': 1},
                'contacts': {'max_num': 1},
            },
        ))
    ], max_num=1, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('contact_info'),
    ]
