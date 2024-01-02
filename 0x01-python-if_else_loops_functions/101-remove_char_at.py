#!/usr/bin/python3

def remove_char_at(str, n):
    str1 = ""
    for x in range(len(str)):
        if x != n:
            str1 += str[x]
    return str1
