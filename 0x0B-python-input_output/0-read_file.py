"""Define a function that read a file"""


def read_file(filename=""):
    """a function that read a UTF8 file"""
    with open(filename, 'r', encoding='utf8') as file:
        content = file.read()
        print(content)
