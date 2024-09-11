from plates import is_valid

def main():
    test_is_valid()


def test_is_valid():
    assert is_valid("cs50") == True
    assert is_valid("ECTO88") == True


def test_is_not_valid():
    assert is_valid("cs05") == False
    assert is_valid("cs50p") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("123456") == False

if __name__ == "__main__":
    main()

