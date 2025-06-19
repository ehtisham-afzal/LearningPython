from hello import say_hello


def test_with_defualt():
    assert say_hello() == "hello world"


def test_with_argument():
    assert say_hello("ehtisham") == "hello ehtisham"


def test_with_many_arguments():
    for phrase in ["world", "country", "state", "ehtisham"]:
        assert say_hello(phrase) == f"hello {phrase}"
