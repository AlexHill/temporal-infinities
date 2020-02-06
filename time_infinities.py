from datetime import datetime, timedelta


class DatetimeInfinity(object):
    def __init__(self, positive):
        self.positive = positive

    def __repr__(self):
        return "DatetimeInfinity(positive=%s)" % self.positive

    def __eq__(self, other):
        return isinstance(other, DatetimeInfinity) and other.positive == self.positive

    def __lt__(self, other):
        if isinstance(other, datetime):
            return not self.positive
        elif isinstance(other, DatetimeInfinity):
            return other.positive and not self.positive
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, datetime):
            return not self.positive
        elif isinstance(other, DatetimeInfinity):
            return not self.positive or self.positive == other.positive
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, datetime):
            return self.positive
        elif isinstance(other, DatetimeInfinity):
            return self.positive and not other.positive
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, datetime):
            return self.positive
        if isinstance(other, DatetimeInfinity):
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
        elif isinstance(other, datetime):
            return TIMEDELTA_POS_INF if self.positive else TIMEDELTA_NEG_INF
        elif isinstance(other, DatetimeInfinity) and self.positive != other.positive:
            return TIMEDELTA_POS_INF if self.positive else TIMEDELTA_NEG_INF
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, datetime):
            return TIMEDELTA_NEG_INF if self.positive else TIMEDELTA_POS_INF
        return NotImplemented

    def __neg__(self):
        return DATETIME_NEG_INF if self.positive else DATETIME_POS_INF


class TimedeltaInfinity(object):
    def __init__(self, positive=True):
        self.positive = positive

    def __repr__(self):
        return "%sTimedeltaInfinity()" % ("" if self.positive else "-")

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
            return DATETIME_POS_INF if self.positive else DATETIME_NEG_INF
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
            return DATETIME_NEG_INF if self.positive else DATETIME_POS_INF
        return NotImplemented

    def __neg__(self):
        return TIMEDELTA_NEG_INF if self.positive else TIMEDELTA_POS_INF


DATETIME_POS_INF = DatetimeInfinity(positive=True)
DATETIME_NEG_INF = DatetimeInfinity(positive=False)
TIMEDELTA_POS_INF = TimedeltaInfinity(positive=True)
TIMEDELTA_NEG_INF = TimedeltaInfinity(positive=False)


def is_finite(value):
    if isinstance(value, (datetime, timedelta)):
        return True
    if isinstance(value, (DatetimeInfinity, TimedeltaInfinity)):
        return False
    else:
        return TypeError("is_finite called with non-temporal type")
