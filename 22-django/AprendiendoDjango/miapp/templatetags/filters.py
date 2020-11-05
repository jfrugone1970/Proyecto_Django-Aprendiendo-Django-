from django import template


register = template.Library()

@register.filter(name='saludo')


def saludo(value, *args):

    largo = ''

    if len(value) <= 0:

        largo = '<p>No has ingresado tu nombre</p>'

    return f"<h1 style='background:green;color:white'>Bienvenido, {value} </h1>"+largo




