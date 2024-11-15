import os
import sys

from cpm_flow import flow


from PIL import Image, UnidentifiedImageError
def main():
    while True:
        # if user invokes CPM interactive flow
        flow.interactive_flow()

        # if user sends direct command
        # flow.direct()

        retry = input("Would you like to generate another color palette? (y/n): ")
        if retry == "y":
            continue
        else:
            sys.exit("Stay creative, bye!")



if __name__ == "__main__":
    main()
