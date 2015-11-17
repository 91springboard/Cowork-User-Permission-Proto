from django import template

register = template.Library()


@register.filter
def has_perm(user, perm_str):
    if user.has_perm(perm_str):
        return 'allow'
    else:
        return 'not-allow'
