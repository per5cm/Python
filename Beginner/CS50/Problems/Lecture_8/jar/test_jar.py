from jar import Jar
import pytest

def test_init():
    # Test default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    # Test invalid capacity
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""  # Initially, no cookies

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()

    # Deposit within capacity
    jar.deposit(5)
    assert jar.size == 5

    # Deposit to exactly fill the jar
    jar.deposit(7)
    assert jar.size == 12

    # Deposit exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)

    # Withdraw within available cookies
    jar.withdraw(5)
    assert jar.size == 5

    # Withdraw exactly all cookies
    jar.withdraw(5)
    assert jar.size == 0

    # Withdraw more cookies than available
    with pytest.raises(ValueError):
        jar.withdraw(1)

