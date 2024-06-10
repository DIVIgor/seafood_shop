from django import template

from wagtail.models import Site

from snippets.models import (
    Footer, Heading, NavbarTitle, BackgroundImage, Favicon
)


register = template.Library()


@register.inclusion_tag('snippets/bg_image.html', takes_context=True)
def get_bg_image(context):
    img = context.get('bg_image', '')

    if not img:
        img = BackgroundImage.objects.first()
        img = img.image if img else ''

    return {'bg_image': img}


@register.inclusion_tag('snippets/heading.html', takes_context=True)
def get_heading(context):
    heading = context.get('heading', '')

    if not heading:
        heading = Heading.objects.filter(live=True).first()
        heading = {
            'upper': heading.localized.upper_heading,
            'lower': heading.localized.lower_heading
        } if heading else ''

    return {'heading': heading}


@register.inclusion_tag('snippets/navbar_title.html', takes_context=True)
def get_navbar_title(context):
    navtitle = context.get('navbar_title', '')

    if not navtitle:
        navtitle = NavbarTitle.objects.filter(live=True).first()
        navtitle = navtitle.localized if navtitle else ''

    return {'navbar_title': navtitle}


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context['request']).root_page.localized


@register.inclusion_tag('snippets/footer_text.html', takes_context=True)
def get_footer_text(context):
    footer = context.get('footer_text', '')

    if not footer:
        footer = Footer.objects.filter(live=True).first()
        footer = footer.localized.content if footer else ''

    return {'footer_text': footer}


@register.simple_tag(takes_context=True)
def get_favicon(context):
    favicon = context.get('favicon', '')

    if not favicon:
        favicon = Favicon.objects.first()
        favicon = favicon.icon if favicon else ''

    return favicon
