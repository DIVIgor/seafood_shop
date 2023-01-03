from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import StreamFieldPanel
from wagtail import blocks


class Contacts(Page):
    schedule = StreamField([
        ('upper_heading', blocks.CharBlock()),
        ('lower_heading', blocks.CharBlock()),
        ('day', blocks.ChoiceBlock(choices=[
            ('sunday', 'Sunday'),
            ('monday', 'Monday'),
            ('tuesday', 'Tuesday'),
            ('wednesday', 'Wednesday'),
            ('thursday', 'Thursday'),
            ('friday', 'Friday'),
            ('saturday', 'Saturday'),
        ])),
        ('worktime_from', blocks.TimeBlock()),
        ('worktime_to', blocks.TimeBlock()),
        ('address_upper', blocks.CharBlock()),
        ('address_lower', blocks.CharBlock()),
        ('short_message', blocks.CharBlock()),
        ('phone', blocks.CharBlock()),
    ], block_counts={
    'upper_heading': {'max_num': 1},
    'lower_heading': {'max_num': 1},
    'day': {'max_num': 7},
    'worktime_from': {'max_num': 7},
    'worktime_to': {'max_num': 7},
    'address_upper': {'max_num': 1},
    'address_lower': {'max_num': 1},
    'short_message': {'max_num': 1},
    'phone': {'max_num': 1},
    }, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('schedule'),
    ]
