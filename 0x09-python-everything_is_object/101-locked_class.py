#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """
    only allows instatiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
