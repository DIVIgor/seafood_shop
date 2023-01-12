from django.db import models

from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class BackgroundImage(models.Model):
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
        ImageChooserPanel('image'),
    ]

    def __str__(self):
        return str(self.image)


@register_snippet
class Header(models.Model):
    upper_header = models.CharField(max_length=255, blank=True)
    lower_header = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('upper_header'),
        FieldPanel('lower_header'),
    ]

    def __str__(self):
        return f'Upper header: {self.upper_header} / Lower header: {self.lower_header}'


@register_snippet
class NavbarTitle(models.Model):
    title = models.CharField(max_length=255, blank=True)
    url = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
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

    class Meta:
        verbose_name_plural = 'footer'

    panels = [
        FieldPanel('content'),
    ]

    def __str__(self):
        return self.content


@register_snippet
class Favicon(models.Model):
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
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return str(self.icon)
