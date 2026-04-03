from kindle_klipper.parser import parse_clippings

def test_parse():
    assert isinstance(parse_clippings("tests/sample.txt"), list)