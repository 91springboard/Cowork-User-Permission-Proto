from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Hub(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return '%s | %s' % (self.name, self.location)


class CoworkUser(models.Model):
    user = models.OneToOneField(User)
    hubs = models.ManyToManyField(Hub)

    class Meta:
        permissions = (
            ("view_coworkuser", "Can view cowork user"),
            # ("change_user", "Can change user's details"),
            # ("add_user", "Can add new user"),
            # ("delete_user", "Can delete user")
        )
