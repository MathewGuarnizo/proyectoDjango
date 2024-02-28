from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo (value):
    largo=''
    if len(value)>=8:
        largo= '<p>Tu nombre es muy largo </p>'
    return f'<h1 style="color:cyan;">Bienvenido, {value}</h1>'+largo

@register.filter(name="subcadena")
def subcadena(value, subcadena):
    if value.startswith(subcadena):
        return value[len(subcadena):]  
    else:
        return ''
