# temporal-infinities

This module provides infinity values compatible with `datetime`, `date`, and `timedelta` in Python 3.

These values are useful to work with when you need to represent time ranges with no beginning or no end. Usually, you would otherwise use `None` to represent these infinite ranges, which leads to extra code to handle those special cases. By using infinity values compatible with Python's built-in types, you eliminate those special cases.
