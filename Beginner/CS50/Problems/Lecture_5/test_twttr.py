from twttr import shorten

def main():
    test_shorten()

def test_shorten(): # character
    assert shorten("twitter") == "twttr"

def test_number():
    assert shorten("1234") == "1234"

if __name__ == "__main__":
    main()