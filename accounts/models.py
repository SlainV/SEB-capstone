from django.contrib.auth.models import AbstractUser
from django.db import models

from publishers.models import Publisher


class User(AbstractUser):
    """
    Custom user model for NewsStream.

    Extends Django's AbstractUser model by adding publisher affiliations
    through a many-to-many relationship and enforcing unique email
    addresses for all users.

    :var publishers: Publishers that the user is affiliated with.
    :vartype publishers: ManyToManyField

    :var email: Unique email address used by the user.
    :vartype email: EmailField
    """
    publishers = models.ManyToManyField(
        Publisher,
        blank=True,
        related_name="users")

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
