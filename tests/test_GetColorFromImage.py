from cpm_app.utils import get_color_from_img


def test_get_rgb_color():
    color = get_color_from_img("tests/images/dawgs.jpeg")
    r, g, b = color
    assert isinstance(color, tuple)
    assert isinstance(r, float)
    assert isinstance(g, float)
    assert isinstance(b, float)
