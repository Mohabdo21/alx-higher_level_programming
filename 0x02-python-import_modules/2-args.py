#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv) - 1
    print(f"{args} argument{'.' if args == 0 else ':'}")

    if args > 0:
        for index, arg in enumerate(argv[1:], start=1):
            print(f"{index}: {arg}")
