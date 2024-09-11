from bank import value

def main():
    test_value()


def test_value():
    assert value("hello") == 0
    assert value("h") == 20
    assert value("nothing") == 100

def test_case_insensitiv():
    assert value("HELLO") == 0
    assert value("Hey") == 20
    assert value("WhaT's UP!") == 100

def test_entire_phrase():
    assert value("hello, how are you?") == 0

if __name__ == "__main__":
    main()