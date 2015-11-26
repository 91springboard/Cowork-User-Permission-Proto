from django import template
from user_app.helper import get_all_locations

register = template.Library()


@register.simple_tag(takes_context=True)
def has_location_perm(context, user, perm_str, obj):
    user_locations = set(get_all_locations(user))
    obj_locations = set(get_all_locations(obj))

    if user_locations.intersection(obj_locations) and user.has_perm(perm_str):
        return 'allow'
    else:
        return 'not-allow'
