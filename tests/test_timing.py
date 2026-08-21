import time


def test_completes_quickly():
    start = time.time()
    sum(range(100000))
    assert time.time() - start < 1.0


def test_race_condition():
    """Simulates a real race: passes about half the time."""
    import random

    worker_finished = random.random() < 0.5
    assert worker_finished, "worker did not finish before the deadline"
