import os


def test_api_token_present():
    token = os.environ.get("API_TOKEN")
    assert token, "API_TOKEN is not set"
    assert token.startswith("tok_")
