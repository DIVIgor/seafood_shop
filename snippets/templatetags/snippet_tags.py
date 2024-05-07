from django import template

from wagtail.models import Site

from snippets.models import (
    Footer, Heading, NavbarTitle, BackgroundImage, Favicon
)


register = template.Library()


@register.inclusion_tag('snippets/bg_image.html', takes_context=True)
def bg_image(context):
    return {
        'bg_image': BackgroundImage.objects.first(),
        'request': context['request'],
    }


@register.inclusion_tag('snippets/heading.html', takes_context=True)
def heading(context):
    return {
        'heading': Heading.objects.first(),
        'request': context['request'],
    }


@register.inclusion_tag('snippets/navbar.html', takes_context=True)
def navbar(context):
    return {
        'navbar': NavbarTitle.objects.first(),
        'request': context['request'],
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


@register.inclusion_tag('snippets/footer_text.html', takes_context=True)
def get_footer_text(context):
    return {
        'footer_text': Footer.objects.all(),
        'request': context['request'],
    }


@register.simple_tag()
def favicon():
    return Favicon.objects.first()
