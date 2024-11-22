import os
import builtins
import unittest
import mimetypes
from unittest.mock import MagicMock, patch

from cpm_app.cli_flow.utils import get_user_file, get_color_scheme, get_color_format

class TestGetUserFile(unittest.TestCase):
    @patch("builtins.input")
    @patch("os.path.isfile")
    @patch("magic.from_file")
    @patch("mimetypes.guess_extension")

    def test_valid_file(self, mock_magic, mock_guess_extension, mock_isfile, mock_input):
        mock_input.return_value = "dawgs.jpeg"
        mock_isfile.return_value = True
        mock_magic.return_valie = "image/jpeg"
        mock_guess_extension.return_value = ".jpeg"

        valid_exts = [".jpg", ".jpeg", ".png"]

        result = get_user_file(valid_exts)
        self.assertEqual(result, "dawgs.jpeg")
        mock_input.assert_called_once()
