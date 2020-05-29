import csv
import datetime as dt
import operator

import pytest
import pytz

from temporal_infinities import (
    DATE_NEG_INF,
    DATE_POS_INF,
    DATETIME_NEG_INF,
    DATETIME_POS_INF,
    TIMEDELTA_NEG_INF,
    TIMEDELTA_POS_INF,
    TemporalInfinity,
    TimedeltaInfinity,
    is_finite,
)

operand_map = {
    (dt.datetime, "NEG_INF"): DATETIME_NEG_INF,
    (dt.datetime, "POS_INF"): DATETIME_POS_INF,
    (dt.datetime, "FINITE"): dt.datetime.now(),
    (dt.datetime, "DELTA_NEG_INF"): TIMEDELTA_NEG_INF,
    (dt.datetime, "DELTA_POS_INF"): TIMEDELTA_POS_INF,
    (dt.datetime, "DELTA_FINITE"): dt.timedelta(),
    (dt.date, "NEG_INF"): DATE_NEG_INF,
    (dt.date, "POS_INF"): DATE_POS_INF,
    (dt.date, "FINITE"): dt.date.today(),
    (dt.date, "DELTA_NEG_INF"): TIMEDELTA_NEG_INF,
    (dt.date, "DELTA_POS_INF"): TIMEDELTA_POS_INF,
    (dt.date, "DELTA_FINITE"): dt.timedelta(),
}


def idfn(val):
    if isinstance(val, dt.datetime):
        return "datetime"
    if isinstance(val, dt.date):
        return "date"
    if isinstance(val, dt.timedelta):
        return "timedelta"
    if isinstance(val, TemporalInfinity):
        return repr(val)
    if isinstance(val, TimedeltaInfinity):
        return repr(val)
    if isinstance(val, type):
        return val.__name__


def gen_params():
    def resolve(ctx, val):
        if val == "True":
            return True
        if val == "False":
            return False
        if val == "":
            return TypeError
        return operand_map[(ctx, val)]

    def uniq(it):
        vals = set()
        for v in it:
            if not v in vals:
                vals.add(v)
                yield v

    with open("test_matrix.csv") as f:
        rdr = csv.reader(f)
        operands = next(rdr)[2:]
        return list(
            uniq(
                (resolve(ctx, lhs), op, resolve(ctx, rhs), resolve(ctx, expect))
                for lhs, op, *results in rdr
                for ctx in set(k[0] for k in operand_map)
                for rhs, expect in zip(operands, results)
            )
        )


@pytest.mark.parametrize(
    ["lhs", "op", "rhs", "expect"], gen_params(), ids=idfn,
)
def test_generated(lhs, op, rhs, expect):
    try:
        result = getattr(operator, op)(lhs, rhs)
    except TypeError:
        assert expect is TypeError
    else:
        assert result == expect


def test_is_finite():
    assert not is_finite(DATETIME_NEG_INF)
    assert not is_finite(DATETIME_POS_INF)
    assert not is_finite(DATE_NEG_INF)
    assert not is_finite(DATE_POS_INF)
    assert not is_finite(TIMEDELTA_NEG_INF)
    assert not is_finite(TIMEDELTA_POS_INF)
    assert is_finite(dt.datetime.now())
    assert is_finite(dt.date.today())
    assert is_finite(dt.timedelta())
    with pytest.raises(TypeError):
        is_finite(True)


def test_timezones():
    naive_time = dt.datetime.utcnow()
    aware_time = pytz.timezone("Australia/Perth").localize(naive_time)
    assert (aware_time + TIMEDELTA_POS_INF).utcoffset() == aware_time.utcoffset()
    assert (naive_time + TIMEDELTA_POS_INF).utcoffset() is None


def test_negation():
    assert -DATETIME_NEG_INF == DATETIME_POS_INF
    assert -DATE_NEG_INF == DATE_POS_INF
    assert -TIMEDELTA_NEG_INF == TIMEDELTA_POS_INF


def test_datetime():
    assert DATETIME_POS_INF.date() == DATE_POS_INF
    assert DATETIME_NEG_INF.date() == DATE_NEG_INF
