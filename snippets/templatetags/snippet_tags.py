from django import template

from snippets.models import Footer, Header, NavbarTitle, BackgroundImage, Favicon


register = template.Library()

@register.inclusion_tag('snippets/bg_image.html', takes_context=True)
def bg_image(context):
    return {
        'bg_image': BackgroundImage.objects.first(),
        'request': context['request'],
    }

@register.inclusion_tag('snippets/header.html', takes_context=True)
def header(context):
    return {
        'header': Header.objects.first(),
        'request': context['request'],
    }

@register.inclusion_tag('snippets/navbar.html', takes_context=True)
def navbar(context):
    return {
        'navbar': NavbarTitle.objects.first(),
        'request': context['request'],
    }

@register.inclusion_tag('snippets/footer.html', takes_context=True)
def footer(context):
    return {
        'footer': Footer.objects.all(),
        'request': context['request'],
    }

@register.simple_tag()
def favicon():
    return Favicon.objects.first()
