# UUN:s1829767
# Name:Jiahui Liu
from msc.rot13 import rot13
from msc.rot13 import rot13_char
def test_rot13_char_a():
    assert "n" == rot13_char("a"), "Unexpected character"

def test_rot13_hello():
    assert "uryyb" == rot13("hello"), "Unexpected character"