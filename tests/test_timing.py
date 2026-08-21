import time


def test_completes_quickly():
    start = time.time()
    sum(range(100000))
    assert time.time() - start < 1.0
