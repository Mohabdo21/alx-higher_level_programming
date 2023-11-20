#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
    except (ValueError, TypeError):
        pass
    except IndexError:
        print("Index out of range")
    finally:
        print()
    return printed_integers
