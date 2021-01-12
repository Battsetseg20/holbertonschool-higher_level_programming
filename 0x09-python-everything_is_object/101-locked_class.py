#!/usr/bin/python3
class LockedClass:
    """Defines a with no class or object attribtue"""

    """Slots are a nice way to work around this space consumption problem.
    Instead of having a dynamic dict that allows adding attributes to
    objects dynamically, slots provide a static structure which prohibits
    additions after the creation of an instance.
    To define slots, you have to define a list with the name __slots__.
    The list has to contain all the attributes, you want to use."""

    __slots__ = ['first_time']
