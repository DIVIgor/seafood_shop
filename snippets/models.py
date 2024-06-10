from django.db import models

from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, PublishingPanel
from wagtail.models import (
    DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin
)
from wagtail.snippets.models import register_snippet


class BasePreviewMixin:
    def get_preview_template(self, request, mode_name):
        return 'base.html'


@register_snippet
class BackgroundImage(BasePreviewMixin,
                      PreviewableMixin,
                      models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    class Meta:
        verbose_name_plural = 'background image'

    panels = [
        FieldPanel('image'),
    ]

    def __str__(self):
        return 'Background image'

    def get_preview_context(self, request, mode_name):
        return {'bg_image': self.image}


@register_snippet
class Heading(BasePreviewMixin,
              DraftStateMixin, RevisionMixin,
              PreviewableMixin, TranslatableMixin,
              models.Model):
    upper_heading = models.CharField(max_length=255, blank=True)
    lower_heading = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('upper_heading'),
        FieldPanel('lower_heading')
    ]

    def __str__(self):
        return 'Heading text'

    def get_preview_context(self, request, mode_name):
        return {'heading': {
            'upper': self.upper_heading,
            'lower': self.lower_heading
        }}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = 'Heading'


@register_snippet
class NavbarTitle(BasePreviewMixin,
                  DraftStateMixin, RevisionMixin,
                  PreviewableMixin, TranslatableMixin,
                  models.Model):
    title_helptext = 'Add here a navigation bar title for small screens'
    navtitle = models.CharField(max_length=255, blank=True,
                                help_text=title_helptext)
    navurl = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('navtitle'),
        PageChooserPanel('navurl'),
    ]

    def __str__(self):
        return 'Title text'

    def get_preview_context(self, request, mode_name):
        return {'navbar_title': {
            'navtitle': self.navtitle, 'navurl': self.navurl
        }}

    class Meta(TranslatableMixin.Meta):
        verbose_name = 'Navbar title'
        verbose_name_plural = 'Navbar title'


@register_snippet
class Footer(BasePreviewMixin,
             DraftStateMixin, RevisionMixin,
             PreviewableMixin, TranslatableMixin,
             models.Model):
    content = StreamField([
        ('footer_text', blocks.RichTextBlock(
            max_length=512,
            features=['h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link'],
            help_text='Use this field to add footer text'
        ))
    ], block_counts={'footer_text': {'max_num': 4}},
        blank=True, use_json_field=True)

    class Meta(TranslatableMixin.Meta):
        verbose_name = 'footer'
        verbose_name_plural = 'footer'

    panels = [
        FieldPanel('content'),
        PublishingPanel()
    ]

    def __str__(self):
        return 'Footer text'

    def get_preview_context(self, request, mode_name):
        return {'footer_text': self.content}


@register_snippet
class Favicon(BasePreviewMixin,
              PreviewableMixin,
              models.Model):
    icon = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    class Meta:
        verbose_name_plural = 'favicon'

    panels = [
        FieldPanel('icon'),
    ]

    def __str__(self):
        return 'Icon'

    def get_preview_context(self, request, mode_name):
        return {'favicon': self.icon}
