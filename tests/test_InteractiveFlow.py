import unittest
from unittest.mock import patch
from cpm_app.cli_flow.utils import get_color_format, get_user_file, get_color_scheme


class TestGetUserFile(unittest.TestCase):
    @patch("builtins.input")
    @patch("os.path.isfile")
    @patch("mimetypes.guess_extension")
    @patch("magic.from_file")
    def test_valid_file(self,
                        mock_magic,
                        mock_guess_extension,
                        mock_isfile,
                        mock_input):
        # Mocking user input
        mock_input.return_value = "valid_image.png"
        # Mocking file existence
        mock_isfile.return_value = True
        # Mocking mimetypes.guess_extension to return .png for valid mime
        mock_guess_extension.return_value = ".png"
        # Mocking magic.from_file to return "image/png" for .png files
        mock_magic.return_value = "image/png"
        # Valid extensions to pass
        valid_exts = [".png", ".jpg", "jpeg"]
        # Call the function
        result = get_user_file(valid_exts)
        # Assert that the result is correct
        self.assertEqual(result, "valid_image.png")
        # Ensure input was called once
        mock_input.assert_called_once()
        # Ensure os.path.isfile was called with the correct file name
        mock_isfile.assert_called_once_with("valid_image.png")
        # Ensure mimetypes.guess_extension was called
        mock_guess_extension.assert_called_once_with("image/png")
        # Ensure magic.from_file was called with the correct file name
        mock_magic.assert_called_once_with("valid_image.png", mime=True)

class TestGetColorScheme(unittest.TestCase):
    @patch("builtins.input")
    def test_get_hsl_scheme(self, mock_input):
        mock_input.return_value = "mono"
        valid_color_schemes = ["mono", "alog", "comp", "scomp"]
        result = get_color_scheme(valid_color_schemes)
        self.assertEqual(result, "mono")
        mock_input.assert_called_once()

class TestGetColorFormat(unittest.TestCase):
    @patch("builtins.input")
    def test_get_rgb_scheme(self, mock_input):
        mock_input.return_value = "r"
        result = get_color_scheme(["r", "h", ""])
        self.assertEqual(result, "r")
        mock_input.assert_called_once()

    @patch("builtins.input")
    def test_get_hsl_scheme(self, mock_input):
        mock_input.return_value = "h"
        result = get_color_scheme(["r", "h", ""])
        self.assertEqual(result, "h")
        mock_input.assert_called_once()

    @patch("builtins.input")
    def test_get_both_schemes(self, mock_input):
        mock_input.return_value = ""
        result = get_color_format(["r", "h", ""])
        self.assertEqual(result, "rh")
        mock_input.assert_called_once()
