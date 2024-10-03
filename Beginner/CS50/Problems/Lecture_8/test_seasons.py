import seasons
import pytest

def test_format():
    with pytest.raises(SystemExit):
        seasons.getDoB("s")



