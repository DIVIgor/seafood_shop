from django.db import models

from wagtail.admin.panels import FieldPanel, PageChooserPanel
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
        FieldPanel('image'),
    ]

    def __str__(self):
        return str(self.image)


@register_snippet
class Heading(models.Model):
    upper_heading = models.CharField(max_length=255, blank=True)
    lower_heading = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('upper_heading'),
        FieldPanel('lower_heading')
    ]

    def __str__(self):
        return f'{self.upper_heading} / {self.lower_heading}'


@register_snippet
class NavbarTitle(models.Model):
    title = models.CharField(max_length=255, blank=True)
    url = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('title'),
        PageChooserPanel('url')
    ]

    def __str__(self):
        return self.title


@register_snippet
class Footer(models.Model):
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'footer'

    panels = [
        FieldPanel('content')
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
        FieldPanel('icon'),
    ]

    def __str__(self):
        return str(self.icon)
