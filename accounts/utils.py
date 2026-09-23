# Permission helpers

def has_role(user, role):
    """
    Check if the current user has a specific role by checking
    if they are a member of the specified role.
    Returns True if they do and False if they do not.

    :param user: The current user object.
    :type user: custom Django User object.
    :param role: The role being checked.
    :type role: Role object.
    :return: True or False depending on the outcome.
    :rtype: bool.
    """
    return user.groups.filter(
        name=role
    ).exists()


def is_reader(user):
    """
    Check if the current user has the 'Reader' role.

    :param user: The current user object.
    :type user: custom Django User object.
    :return: True if the user has the Reader role, False otherwise.
    :rtype: bool.
    """
    return has_role(
        user,
        "Reader"
    )


def is_editor(user):
    return has_role(
        user,
        "Editor"
    )


def is_journalist(user):
    return has_role(
        user,
        "Journalist"
    )


def is_publisher_manager(user):
    return has_role(
        user,
        "Publisher Manager"
    )


def is_administrator(self):
    """Check if the current user has a specific role."""
    return self.groups.filter(name="Administrator").exists()
