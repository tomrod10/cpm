import unittest
from unittest.mock import patch


from cpm_app.cli_flow.utils import get_user_file


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
        mock_magic.return_value = "image/png"  # or whatever magic returns for .png

        # Valid extensions to pass
        valid_exts = [".png", ".jpg"]

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


    # @patch("builtins.input")
    # @patch("os.path.isfile")
    # def test_invalid_file():
    #     ...
