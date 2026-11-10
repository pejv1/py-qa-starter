# classify_temp: your code
def classify_temp(celsius):
    """Return "cold" below 10, "ok" from 10 to 25 (both included), "hot" above 25."""
    if celsius >= 10 and celsius <= 25:
        return "ok"
    if celsius < 10:
        return "cold"
    else:
        return "hot"


# ---- helpers and given tests (do not edit) ----
def check(got, expected, label):
    assert got == expected, f"{label} returned {got!r}, expected {expected!r}"


def raises(exc, fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except exc as e:
        return e
    raise AssertionError(f"{getattr(fn, '__name__', 'call')}{args!r} did not raise {exc.__name__}")


def test_cold():
    """below 10 is cold"""
    check(classify_temp(-5), "cold", "classify_temp(-5)")
    check(classify_temp(9.9), "cold", "classify_temp(9.9)")


def test_boundaries_are_ok():
    """10 and 25 are both ok"""
    check(classify_temp(10), "ok", "classify_temp(10)")
    check(classify_temp(25), "ok", "classify_temp(25)")


def test_middle():
    """21.5 is ok"""
    check(classify_temp(21.5), "ok", "classify_temp(21.5)")


def test_hot():
    """above 25 is hot"""
    check(classify_temp(25.1), "hot", "classify_temp(25.1)")
    check(classify_temp(40), "hot", "classify_temp(40)")


if __name__ == "__main__":
    import sys
    failed = 0
    for _name, _fn in list(globals().items()):
        if _name.startswith("test_") and callable(_fn):
            try:
                _fn()
                print("PASS", _name)
            except Exception as _e:
                failed += 1
                print("FAIL", _name, "-", type(_e).__name__, _e)
    sys.exit(1 if failed else 0)