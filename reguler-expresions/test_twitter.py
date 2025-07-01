from twitter import get_twitter_username
import pytest


def test_full_url():
    assert (
        get_twitter_username("https://www.twitter.com/ehtisham_dev") == "ehtisham_dev"
    )


def test_http():
    assert get_twitter_username("http://www.twitter.com/ehtisham_dev") == "ehtisham_dev"


def test_https():
    assert get_twitter_username("https://twitter.com/ehtisham_dev") == "ehtisham_dev"


def test_without_protocol():
    assert get_twitter_username("www.twitter.com/ehtisham_dev") == "ehtisham_dev"


def test_without_protocol_and_www():
    assert get_twitter_username("twitter.com/ehtisham_dev") == "ehtisham_dev"


def test_x_domain():
    assert get_twitter_username("https://x.com/ehtisham_dev") == "ehtisham_dev"


def test_without_username():
    assert get_twitter_username("https://x.com/") == None  # noqa: E711
    # with pytest.raises(AttributeError):
    #     get_twitter_username("https://x.com/")


def test_username_validation():
    assert get_twitter_username("https://twitter.com/ehtisham?dev") == None  # noqa: E711
