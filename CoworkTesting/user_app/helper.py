
from django.contrib.auth.models import User


def get_all_locations(obj):
    if isinstance(obj, User):
        hubs = obj.coworkuser.hubs.all()
        return [h.location for h in hubs]
    else:
        return [obj.hub.location]
