import sys


def shrink(text):
    print(text[:8])


def enlarge(text):
    text += "Z" * (8 - len(text))
    print(text)


if len(sys.argv) < 2:
    print("none")
else:
    for argument in sys.argv[1:]:
        if len(argument) > 8:
            shrink(argument)
        elif len(argument) < 8:
            enlarge(argument)
        else:
            print(argument)