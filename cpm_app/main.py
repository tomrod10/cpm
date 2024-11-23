import os
import sys

from cli_flow.flow import interactive_flow


from PIL import Image, UnidentifiedImageError
def main():
    while True:
        # if user invokes CPM interactive flow
        interactive_flow()

        # if user sends direct command
        # flow.direct()

        # TODO: move this to only be accesible from the interactive flow
        retry = input("Would you like to generate another color palette? (y/n): ")
        if retry == "y":
            continue
        else:
            sys.exit("Stay creative, bye!")



if __name__ == "__main__":
    main()
