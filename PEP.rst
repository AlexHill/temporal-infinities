Abstract
========

This PEP proposes to add infinite temporal (date, datetime and timedelta) types to the standard library.

Motivation
==========

Infinity is a natural and useful concept to employ when manipulating dates and times. Nearly all code that handles time will have to model the idea of a period of time with its lower or upper bound or both undefined. Treating these undefined bounds as infinity facilitates the production of simple and consistent code to handle time.

Consider a class representing a date range, with a `start` and an `end`::

    @dataclass
    class DateRange:
        start: date
        end: date

Say you want to represent the range "forever, from October 5th 2020". How do you represent the `end` of that range? There are a couple of obvious options available to you: you could use `date.max` or some other arbitrarily large `date`, or you could use `None`.

Let's write a function that takes a DateRange and returns `True` if it contains today's date, `False` otherwise::

    def contains_today(dr):
        return dr.start <= date.today() < dr.end

    >>> contains_today(DateRange(start=date.today(), end=None))
    TypeError: '<' not supported between instances of 'datetime.date' and 'NoneType'

You can't compare None with a date, so immediately we have to special case `None`::

    def contains_today(dr):
        today = date.today()
        if dr.start is None and dr.end is None:
            return True
        if dr.start is None:
            return today < dr.end
        if dr.end is None:
            return dr.start <= today
        return dr.start <= today < dr.end

If we use `date.max`, our original function works just fine, because it's a real finite date and can be compared like any other. But now we're asked to write a function that returns a DateRange one week later than the one passed in::

    def one_week_later(dr):
        return DateRange(
            start=dr.start + timedelta(days=7),
            end=dr.end + timedelta(days=7),
        )

    >>> one_week_later(DateRange(start=date(2020, 10, 5), end=date.max))
    OverflowError: date value out of range

You can't add anything to `date.max`. Again, you need to handle the special value specially. In desperation, you might try adding


This special-casing is required for all sorts of operations - checking if a range overlaps another, checking if a particular date falls within a given range, calculating the duration between between two datetimes, and so on.

Temporal infinity types are designed to make these situations simpler. They are mostly interoperable with the existing types, and implement comparison and arithmetic operators in a sensible way::

    >>> one_week_later(DateRange(start=date(2020, 10, 5), end=date.inf_future))
    DateRange(start=datetime.date(2020, 10, 12), end=datetime.date.inf_future)



Rationale
=========

[Describe why particular design decisions were made.]


Specification
=============

[Describe the syntax and semantics of any new language feature.]


Backwards Compatibility
=======================

[Describe potential impact and severity on pre-existing code.]


Security Implications
=====================

[How could a malicious user take advantage of this new feature?]


How to Teach This
=================

[How to teach users, new and experienced, how to apply the PEP to their work.]


Reference Implementation
========================

[Link to any existing implementation and details about its state, e.g. proof-of-concept.]


Rejected Ideas
==============

[Why certain ideas that were brought while discussing this PEP were not ultimately pursued.]


Open Issues
===========

[Any points that are still being decided/discussed.]


References
==========

[A collection of URLs used as references through the PEP.]


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
