import datetime as dt

from pytest import raises

from siqtv.player.time_infinities import DATETIME_NEG_INF, DATETIME_POS_INF, TIMEDELTA_NEG_INF, TIMEDELTA_POS_INF


def test_infinities():
    datetime = dt.datetime.now()
    timedelta = dt.timedelta(days=1)

    assert not DATETIME_NEG_INF < DATETIME_NEG_INF
    assert DATETIME_NEG_INF <= DATETIME_NEG_INF
    assert not DATETIME_NEG_INF > DATETIME_NEG_INF
    assert DATETIME_NEG_INF >= DATETIME_NEG_INF
    assert DATETIME_NEG_INF == DATETIME_NEG_INF
    assert not DATETIME_NEG_INF != DATETIME_NEG_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF + DATETIME_NEG_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF - DATETIME_NEG_INF

    assert DATETIME_NEG_INF < DATETIME_POS_INF
    assert DATETIME_NEG_INF <= DATETIME_POS_INF
    assert not DATETIME_NEG_INF > DATETIME_POS_INF
    assert not DATETIME_NEG_INF >= DATETIME_POS_INF
    assert not DATETIME_NEG_INF == DATETIME_POS_INF
    assert DATETIME_NEG_INF != DATETIME_POS_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF + DATETIME_POS_INF
    assert DATETIME_NEG_INF - DATETIME_POS_INF == TIMEDELTA_NEG_INF

    with raises(TypeError):
        assert DATETIME_NEG_INF < TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF <= TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF > TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF >= TIMEDELTA_NEG_INF
    assert not DATETIME_NEG_INF == TIMEDELTA_NEG_INF
    assert DATETIME_NEG_INF != TIMEDELTA_NEG_INF
    assert DATETIME_NEG_INF + TIMEDELTA_NEG_INF == DATETIME_NEG_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF - TIMEDELTA_NEG_INF

    with raises(TypeError):
        assert DATETIME_NEG_INF < TIMEDELTA_POS_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF <= TIMEDELTA_POS_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF > TIMEDELTA_POS_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF >= TIMEDELTA_POS_INF
    assert not DATETIME_NEG_INF == TIMEDELTA_POS_INF
    assert DATETIME_NEG_INF != TIMEDELTA_POS_INF
    with raises(TypeError):
        assert DATETIME_NEG_INF + TIMEDELTA_POS_INF
    assert DATETIME_NEG_INF - TIMEDELTA_POS_INF == DATETIME_NEG_INF

    assert DATETIME_NEG_INF < datetime
    assert DATETIME_NEG_INF <= datetime
    assert not DATETIME_NEG_INF > datetime
    assert not DATETIME_NEG_INF >= datetime
    assert not DATETIME_NEG_INF == datetime
    assert DATETIME_NEG_INF != datetime
    with raises(TypeError):
        assert DATETIME_NEG_INF + datetime
    assert DATETIME_NEG_INF - datetime == TIMEDELTA_NEG_INF

    with raises(TypeError):
        assert DATETIME_NEG_INF < timedelta
    with raises(TypeError):
        assert DATETIME_NEG_INF <= timedelta
    with raises(TypeError):
        assert DATETIME_NEG_INF > timedelta
    with raises(TypeError):
        assert DATETIME_NEG_INF >= timedelta
    assert not DATETIME_NEG_INF == timedelta
    assert DATETIME_NEG_INF != timedelta
    assert DATETIME_NEG_INF + timedelta == DATETIME_NEG_INF
    assert DATETIME_NEG_INF - timedelta == DATETIME_NEG_INF

    assert not DATETIME_POS_INF < DATETIME_NEG_INF
    assert not DATETIME_POS_INF <= DATETIME_NEG_INF
    assert DATETIME_POS_INF > DATETIME_NEG_INF
    assert DATETIME_POS_INF >= DATETIME_NEG_INF
    assert not DATETIME_POS_INF == DATETIME_NEG_INF
    assert DATETIME_POS_INF != DATETIME_NEG_INF
    with raises(TypeError):
        assert DATETIME_POS_INF + DATETIME_NEG_INF
    assert DATETIME_POS_INF - DATETIME_NEG_INF == TIMEDELTA_POS_INF

    assert not DATETIME_POS_INF < DATETIME_POS_INF
    assert DATETIME_POS_INF <= DATETIME_POS_INF
    assert not DATETIME_POS_INF > DATETIME_POS_INF
    assert DATETIME_POS_INF >= DATETIME_POS_INF
    assert DATETIME_POS_INF == DATETIME_POS_INF
    assert not DATETIME_POS_INF != DATETIME_POS_INF
    with raises(TypeError):
        assert DATETIME_POS_INF + DATETIME_POS_INF
    with raises(TypeError):
        assert DATETIME_POS_INF - DATETIME_POS_INF

    with raises(TypeError):
        assert DATETIME_POS_INF < TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert DATETIME_POS_INF <= TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert DATETIME_POS_INF > TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert DATETIME_POS_INF >= TIMEDELTA_NEG_INF
    assert not DATETIME_POS_INF == TIMEDELTA_NEG_INF
    assert DATETIME_POS_INF != TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert DATETIME_POS_INF + TIMEDELTA_NEG_INF
    assert DATETIME_POS_INF - TIMEDELTA_NEG_INF == DATETIME_POS_INF

    with raises(TypeError):
        assert DATETIME_POS_INF < TIMEDELTA_POS_INF
    with raises(TypeError):
        assert DATETIME_POS_INF <= TIMEDELTA_POS_INF
    with raises(TypeError):
        assert DATETIME_POS_INF > TIMEDELTA_POS_INF
    with raises(TypeError):
        assert DATETIME_POS_INF >= TIMEDELTA_POS_INF
    assert not DATETIME_POS_INF == TIMEDELTA_POS_INF
    assert DATETIME_POS_INF != TIMEDELTA_POS_INF
    assert DATETIME_POS_INF + TIMEDELTA_POS_INF == DATETIME_POS_INF
    with raises(TypeError):
        assert DATETIME_POS_INF - TIMEDELTA_POS_INF

    assert not DATETIME_POS_INF < datetime
    assert not DATETIME_POS_INF <= datetime
    assert DATETIME_POS_INF > datetime
    assert DATETIME_POS_INF >= datetime
    assert not DATETIME_POS_INF == datetime
    assert DATETIME_POS_INF != datetime
    with raises(TypeError):
        assert DATETIME_POS_INF + datetime
    assert DATETIME_POS_INF - datetime == TIMEDELTA_POS_INF

    with raises(TypeError):
        assert DATETIME_POS_INF < timedelta
    with raises(TypeError):
        assert DATETIME_POS_INF <= timedelta
    with raises(TypeError):
        assert DATETIME_POS_INF > timedelta
    with raises(TypeError):
        assert DATETIME_POS_INF >= timedelta
    assert not DATETIME_POS_INF == timedelta
    assert DATETIME_POS_INF != timedelta
    assert DATETIME_POS_INF + timedelta == DATETIME_POS_INF
    assert DATETIME_POS_INF - timedelta == DATETIME_POS_INF

    with raises(TypeError):
        assert TIMEDELTA_NEG_INF < DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF <= DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF > DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF >= DATETIME_NEG_INF
    assert not TIMEDELTA_NEG_INF == DATETIME_NEG_INF
    assert TIMEDELTA_NEG_INF != DATETIME_NEG_INF
    assert TIMEDELTA_NEG_INF + DATETIME_NEG_INF == DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF - DATETIME_NEG_INF

    with raises(TypeError):
        assert TIMEDELTA_NEG_INF < DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF <= DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF > DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF >= DATETIME_POS_INF
    assert not TIMEDELTA_NEG_INF == DATETIME_POS_INF
    assert TIMEDELTA_NEG_INF != DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF + DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF - DATETIME_POS_INF

    assert not TIMEDELTA_NEG_INF < TIMEDELTA_NEG_INF
    assert TIMEDELTA_NEG_INF <= TIMEDELTA_NEG_INF
    assert not TIMEDELTA_NEG_INF > TIMEDELTA_NEG_INF
    assert TIMEDELTA_NEG_INF >= TIMEDELTA_NEG_INF
    assert TIMEDELTA_NEG_INF == TIMEDELTA_NEG_INF
    assert not TIMEDELTA_NEG_INF != TIMEDELTA_NEG_INF
    assert TIMEDELTA_NEG_INF + TIMEDELTA_NEG_INF == TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF - TIMEDELTA_NEG_INF

    assert TIMEDELTA_NEG_INF < TIMEDELTA_POS_INF
    assert TIMEDELTA_NEG_INF <= TIMEDELTA_POS_INF
    assert not TIMEDELTA_NEG_INF > TIMEDELTA_POS_INF
    assert not TIMEDELTA_NEG_INF >= TIMEDELTA_POS_INF
    assert not TIMEDELTA_NEG_INF == TIMEDELTA_POS_INF
    assert TIMEDELTA_NEG_INF != TIMEDELTA_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF + TIMEDELTA_POS_INF
    assert TIMEDELTA_NEG_INF - TIMEDELTA_POS_INF == TIMEDELTA_NEG_INF

    with raises(TypeError):
        assert TIMEDELTA_NEG_INF < datetime
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF <= datetime
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF > datetime
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF >= datetime
    assert not TIMEDELTA_NEG_INF == datetime
    assert TIMEDELTA_NEG_INF != datetime
    assert TIMEDELTA_NEG_INF + datetime == DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_NEG_INF - datetime

    assert TIMEDELTA_NEG_INF < timedelta
    assert TIMEDELTA_NEG_INF <= timedelta
    assert not TIMEDELTA_NEG_INF > timedelta
    assert not TIMEDELTA_NEG_INF >= timedelta
    assert not TIMEDELTA_NEG_INF == timedelta
    assert TIMEDELTA_NEG_INF != timedelta
    assert TIMEDELTA_NEG_INF + timedelta == TIMEDELTA_NEG_INF
    assert TIMEDELTA_NEG_INF - timedelta == TIMEDELTA_NEG_INF

    with raises(TypeError):
        assert TIMEDELTA_POS_INF < DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF <= DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF > DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF >= DATETIME_NEG_INF
    assert not TIMEDELTA_POS_INF == DATETIME_NEG_INF
    assert TIMEDELTA_POS_INF != DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF + DATETIME_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF - DATETIME_NEG_INF

    with raises(TypeError):
        assert TIMEDELTA_POS_INF < DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF <= DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF > DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF >= DATETIME_POS_INF
    assert not TIMEDELTA_POS_INF == DATETIME_POS_INF
    assert TIMEDELTA_POS_INF != DATETIME_POS_INF
    assert TIMEDELTA_POS_INF + DATETIME_POS_INF == DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF - DATETIME_POS_INF

    assert not TIMEDELTA_POS_INF < TIMEDELTA_NEG_INF
    assert not TIMEDELTA_POS_INF <= TIMEDELTA_NEG_INF
    assert TIMEDELTA_POS_INF > TIMEDELTA_NEG_INF
    assert TIMEDELTA_POS_INF >= TIMEDELTA_NEG_INF
    assert not TIMEDELTA_POS_INF == TIMEDELTA_NEG_INF
    assert TIMEDELTA_POS_INF != TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF + TIMEDELTA_NEG_INF
    assert TIMEDELTA_POS_INF - TIMEDELTA_NEG_INF == TIMEDELTA_POS_INF

    assert not TIMEDELTA_POS_INF < TIMEDELTA_POS_INF
    assert TIMEDELTA_POS_INF <= TIMEDELTA_POS_INF
    assert not TIMEDELTA_POS_INF > TIMEDELTA_POS_INF
    assert TIMEDELTA_POS_INF >= TIMEDELTA_POS_INF
    assert TIMEDELTA_POS_INF == TIMEDELTA_POS_INF
    assert not TIMEDELTA_POS_INF != TIMEDELTA_POS_INF
    assert TIMEDELTA_POS_INF + TIMEDELTA_POS_INF == TIMEDELTA_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF - TIMEDELTA_POS_INF

    with raises(TypeError):
        assert TIMEDELTA_POS_INF < datetime
    with raises(TypeError):
        assert TIMEDELTA_POS_INF <= datetime
    with raises(TypeError):
        assert TIMEDELTA_POS_INF > datetime
    with raises(TypeError):
        assert TIMEDELTA_POS_INF >= datetime
    assert not TIMEDELTA_POS_INF == datetime
    assert TIMEDELTA_POS_INF != datetime
    assert TIMEDELTA_POS_INF + datetime == DATETIME_POS_INF
    with raises(TypeError):
        assert TIMEDELTA_POS_INF - datetime

    assert not TIMEDELTA_POS_INF < timedelta
    assert not TIMEDELTA_POS_INF <= timedelta
    assert TIMEDELTA_POS_INF > timedelta
    assert TIMEDELTA_POS_INF >= timedelta
    assert not TIMEDELTA_POS_INF == timedelta
    assert TIMEDELTA_POS_INF != timedelta
    assert TIMEDELTA_POS_INF + timedelta == TIMEDELTA_POS_INF
    assert TIMEDELTA_POS_INF - timedelta == TIMEDELTA_POS_INF

    assert not datetime < DATETIME_NEG_INF
    assert not datetime <= DATETIME_NEG_INF
    assert datetime > DATETIME_NEG_INF
    assert datetime >= DATETIME_NEG_INF
    assert not datetime == DATETIME_NEG_INF
    assert datetime != DATETIME_NEG_INF
    with raises(TypeError):
        assert datetime + DATETIME_NEG_INF
    assert datetime - DATETIME_NEG_INF == TIMEDELTA_POS_INF

    assert datetime < DATETIME_POS_INF
    assert datetime <= DATETIME_POS_INF
    assert not datetime > DATETIME_POS_INF
    assert not datetime >= DATETIME_POS_INF
    assert not datetime == DATETIME_POS_INF
    assert datetime != DATETIME_POS_INF
    with raises(TypeError):
        assert datetime + DATETIME_POS_INF
    assert datetime - DATETIME_POS_INF == TIMEDELTA_NEG_INF

    with raises(TypeError):
        assert datetime < TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert datetime <= TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert datetime > TIMEDELTA_NEG_INF
    with raises(TypeError):
        assert datetime >= TIMEDELTA_NEG_INF
    assert not datetime == TIMEDELTA_NEG_INF
    assert datetime != TIMEDELTA_NEG_INF
    assert datetime + TIMEDELTA_NEG_INF == DATETIME_NEG_INF
    assert datetime - TIMEDELTA_NEG_INF == DATETIME_POS_INF

    with raises(TypeError):
        assert datetime < TIMEDELTA_POS_INF
    with raises(TypeError):
        assert datetime <= TIMEDELTA_POS_INF
    with raises(TypeError):
        assert datetime > TIMEDELTA_POS_INF
    with raises(TypeError):
        assert datetime >= TIMEDELTA_POS_INF
    assert not datetime == TIMEDELTA_POS_INF
    assert datetime != TIMEDELTA_POS_INF
    assert datetime + TIMEDELTA_POS_INF == DATETIME_POS_INF
    assert datetime - TIMEDELTA_POS_INF == DATETIME_NEG_INF

    with raises(TypeError):
        assert timedelta < DATETIME_NEG_INF
    with raises(TypeError):
        assert timedelta <= DATETIME_NEG_INF
    with raises(TypeError):
        assert timedelta > DATETIME_NEG_INF
    with raises(TypeError):
        assert timedelta >= DATETIME_NEG_INF
    assert not timedelta == DATETIME_NEG_INF
    assert timedelta != DATETIME_NEG_INF
    assert timedelta + DATETIME_NEG_INF == DATETIME_NEG_INF
    with raises(TypeError):
        assert timedelta - DATETIME_NEG_INF

    with raises(TypeError):
        assert timedelta < DATETIME_POS_INF
    with raises(TypeError):
        assert timedelta <= DATETIME_POS_INF
    with raises(TypeError):
        assert timedelta > DATETIME_POS_INF
    with raises(TypeError):
        assert timedelta >= DATETIME_POS_INF
    assert not timedelta == DATETIME_POS_INF
    assert timedelta != DATETIME_POS_INF
    assert timedelta + DATETIME_POS_INF == DATETIME_POS_INF
    with raises(TypeError):
        assert timedelta - DATETIME_POS_INF

    assert not timedelta < TIMEDELTA_NEG_INF
    assert not timedelta <= TIMEDELTA_NEG_INF
    assert timedelta > TIMEDELTA_NEG_INF
    assert timedelta >= TIMEDELTA_NEG_INF
    assert not timedelta == TIMEDELTA_NEG_INF
    assert timedelta != TIMEDELTA_NEG_INF
    assert timedelta + TIMEDELTA_NEG_INF == TIMEDELTA_NEG_INF
    assert timedelta - TIMEDELTA_NEG_INF == TIMEDELTA_POS_INF

    assert timedelta < TIMEDELTA_POS_INF
    assert timedelta <= TIMEDELTA_POS_INF
    assert not timedelta > TIMEDELTA_POS_INF
    assert not timedelta >= TIMEDELTA_POS_INF
    assert not timedelta == TIMEDELTA_POS_INF
    assert timedelta != TIMEDELTA_POS_INF
    assert timedelta + TIMEDELTA_POS_INF == TIMEDELTA_POS_INF
    assert timedelta - TIMEDELTA_POS_INF == TIMEDELTA_NEG_INF
