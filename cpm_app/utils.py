import os


def is_valid_file(file_name):
    file_exists = os.path.isfile(file_name)
    valid_ext = ["jpg", "jpeg", "png"]
    file_ext = file_name.split(".", 1)[1] # TODO: check for str without "." case
    while True:
        if not file_exists:
            print("File not found! Try again")
            continue
        if file_ext not in valid_ext:
            print("Invalid file format! Try again")
            continue
        break
    return True

def is_valid_color_scheme(color_scheme):
    color_schemes = ["mono", "alog", "comp", "scomp"]
    while(color_scheme not in color_schemes):
        print("Invalid color scheme! Try again")
    return True

def get_color_scheme(): #WIP
    try:
        cs = input("Enter color scheme you wish to use: ")
    except BaseException as e:
        print(e)
