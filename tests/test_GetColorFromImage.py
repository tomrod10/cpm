from cpm_app.utils import get_color_from_img

#test with dawgs.jpeg
def test_get_rgb_color():
    rgb = get_color_from_img("dawgs.jpeg")
    r, g, b = rgb
    assert isinstance(rgb, tuple)
    assert isinstance(r, float)
    assert isinstance(g, float)
    assert isinstance(b, float)

#test with grayscale image
def test_get_grayscale_color():
    grayscale = get_color_from_img("grayscale.png")
    assert isinstance(grayscale, float)
