import os
import sys
import magic
import mimetypes
import platform

from PIL import Image, UnidentifiedImageError

def main():
    device_os = platform.system()
    print(f"OS: [{device_os}]")
    print(f"Current directory: {os.getcwd()}")

    while True:
        try:
            file_name = input("Enter name of the file you wish to generate a palette from: ")
            image = Image.open(file_name)

            if not len(file_name):
                raise ValueError("Invalid file path")

        except ValueError as e:
            print(e, file=sys.stdout)

        sys.exit()

if __name__ != "__main__":
    main()
