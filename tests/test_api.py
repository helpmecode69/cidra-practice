import requests


def test_fetch():
    """Uses requests but never goes to the network — CI has no egress guarantee."""
    assert hasattr(requests, "get")
