from cpm_app.utils import make_monochromatic_color_palette

TEST_HLS_COLOR = (0.37, 0.27, 0.20)

# test for return value in single format rgb
def test_palette_in_rgb():
    cp = make_monochromatic_color_palette(TEST_HLS_COLOR, 'r')
    assert len(cp) == 2
    assert len(cp['r']) == 5
    assert len(cp['r'][0]) == 3
    assert isinstance(cp['r'][0][0], int)


# test for return value in single format hls (should still return in rgb)
def test_palette_in_hls():
    cp = make_monochromatic_color_palette(TEST_HLS_COLOR, 'h')
    assert len(cp) == 2
    assert len(cp['h']) == 5
    assert len(cp['h'][0]) == 3
    assert isinstance(cp['h'][0][0], int)

# test for return value in both formats dict with rgb and hls
def test_palette_in_both_formats():
    cp = make_monochromatic_color_palette(TEST_HLS_COLOR, 'rh')
    assert len(cp) == 2
    assert len(cp['h']) == 5
    assert len(cp['r']) == 5
    assert len(cp['h'][0]) == 3
    assert len(cp['r'][0]) == 3
    assert isinstance(cp['h'][0][0], int)
    assert isinstance(cp['r'][0][0], int)
