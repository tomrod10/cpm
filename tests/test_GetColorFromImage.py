from cpm_app.utils import get_color_from_img


def test_get_rgb_color():
    rgb = get_color_from_img("tests/images/dawgs.jpeg")
    r, g, b = rgb
    assert isinstance(rgb, tuple)
    assert isinstance(r, float)
    assert isinstance(g, float)
    assert isinstance(b, float)
