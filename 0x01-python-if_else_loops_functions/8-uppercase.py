#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - 32), end='\n')
        else:
            print("{:c}".format(ord(char)), end='\n')
