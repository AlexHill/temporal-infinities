from datetime import date, datetime, timedelta


class TemporalInfinity(object):

    comparison_type = None

    __slots__ = ["positive", "tzinfo"]

    def __init__(self, positive, tzinfo=None):
        self.positive = positive
        self.tzinfo = tzinfo

    def __hash__(self):
        return hash((self.positive, self.tzinfo))

    def __repr__(self):
        return "%s_%s_INF" % (
            self.comparison_type.__name__.upper(),
            "POS" if self.positive else "NEG",
        )

    def utcoffset(self):
        if self.tzinfo is None:
            return None
        return self.tzinfo.utcoffset(self)

    def __eq__(self, other):
        return (
            isinstance(self, other.__class__)
            and other.positive == self.positive
            and other.tzinfo == self.tzinfo
        )

    def __lt__(self, other):
        if isinstance(other, self.comparison_type):
            return not self.positive
        elif isinstance(self, other.__class__):
            return other.positive and not self.positive
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, self.comparison_type):
            return not self.positive
        elif isinstance(self, other.__class__):
            return not self.positive or self.positive == other.positive
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.comparison_type):
            return self.positive
        elif isinstance(self, other.__class__):
            return self.positive and not other.positive
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, self.comparison_type):
            return self.positive
        if isinstance(self, other.__class__):
            return self.positive or self.positive == other.positive
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, timedelta):
            return self
        elif isinstance(other, TimedeltaInfinity) and self.positive == other.positive:
            return self
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, timedelta):
            return self
        elif isinstance(other, TimedeltaInfinity) and self.positive != other.positive:
            return self
        elif isinstance(other, self.comparison_type):
            return TimedeltaInfinity(self.positive)
        elif isinstance(self, other.__class__) and self.positive != other.positive:
            return TimedeltaInfinity(self.positive)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, self.comparison_type):
            return TimedeltaInfinity(not self.positive)
        return NotImplemented

    def __neg__(self):
        return self.__class__(not self.positive)


class DateInfinity(TemporalInfinity):
    comparison_type = date

    def __init__(self, positive):
        super(DateInfinity, self).__init__(positive)


class DatetimeInfinity(TemporalInfinity):
    comparison_type = datetime

    def date(self):
        return DateInfinity(self.positive)


class TimedeltaInfinity(object):

    __slots__ = ["positive"]

    def __init__(self, positive=True):
        self.positive = positive

    def __hash__(self):
        return hash(self.positive)

    def __repr__(self):
        return ("" if self.positive else "-") + "TIMEDELTA_INF"

    def __eq__(self, other):
        return isinstance(other, TimedeltaInfinity) and other.positive == self.positive

    def __lt__(self, other):
        if isinstance(other, timedelta):
            return not self.positive
        elif isinstance(other, TimedeltaInfinity):
            return other.positive and not self.positive
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, timedelta):
            return not self.positive
        elif isinstance(other, TimedeltaInfinity):
            return not self.positive or self.positive == other.positive
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, timedelta):
            return self.positive
        elif isinstance(other, TimedeltaInfinity):
            return self.positive and not other.positive
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, timedelta):
            return self.positive
        if isinstance(other, TimedeltaInfinity):
            return self.positive or self.positive == other.positive
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, timedelta):
            return self
        elif isinstance(other, datetime):
            return DatetimeInfinity(self.positive, tzinfo=other.tzinfo)
        elif isinstance(other, date):
            return DateInfinity(self.positive)
        elif isinstance(other, TimedeltaInfinity) and self.positive == other.positive:
            return self
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, timedelta):
            return self
        elif isinstance(other, TimedeltaInfinity) and self.positive != other.positive:
            return self
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, timedelta):
            return -self
        elif isinstance(other, datetime):
            return DatetimeInfinity(not self.positive, tzinfo=other.tzinfo)
        elif isinstance(other, date):
            return DateInfinity(not self.positive)
        return NotImplemented

    def __neg__(self):
        return TimedeltaInfinity(not self.positive)


DATE_INF_FUTURE = DateInfinity(positive=True)
DATE_INF_PAST = DateInfinity(positive=False)
DATETIME_INF_FUTURE = DatetimeInfinity(positive=True)
DATETIME_INF_PAST = DatetimeInfinity(positive=False)
TIMEDELTA_INF = TimedeltaInfinity(positive=True)


def is_finite(value):
    if isinstance(value, (date, datetime, timedelta)):
        return True
    if isinstance(value, (TemporalInfinity, TimedeltaInfinity)):
        return False
    else:
        raise TypeError("is_finite called with non-temporal type")
