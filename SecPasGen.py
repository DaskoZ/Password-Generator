#! /usr/bin/python3
import random as rd
import argparse
import re
import clipboard as c

    # Password_generator!
def pass_gen(length, uppers, numbers, symbols):   
    combine = "abcdefghijklmnopqrstuvwxyz"
    l_up = combine.upper()
    num  = "0123456789"
    symb = "!@#$%^&*"
    
    if uppers:
        combine += l_up
    if numbers:
        combine += num
    if symbols:
        combine += symb

    password = ''
    for _ in range(length):
        password += combine[rd.randint(0,len(combine)-1)]

    if matched_pass(password, uppers, numbers, symbols):
        return password
    else:
        return pass_gen(length, uppers, numbers, symbols)

    #   Returns True if password satisfy the requirements! 
def matched_pass(pw, uppers, nums, symb):
    f = True
    if uppers:
        if not re.search(r"[A-Z]", pw):
            f = False

    if nums:
        if not re.search(r"\d", pw):
            f = False

    if symb:
        if not re.search(r"[!@#$%^&*]", pw):
            f = False

    if not re.search(r"[a-z]", pw):
        f = False

    return f
    
    #   Creating arguments
parser = argparse.ArgumentParser() 
parser.add_argument("length", help="Password length[min='8']", type=int)
parser.add_argument("-u","--uppers", action='store_true', default=argparse.SUPPRESS, help='Include upper-case letters')
parser.add_argument("-n", "--nums", action='store_true', default=argparse.SUPPRESS, help='Include numbers')
parser.add_argument("-sy","--symb", action='store_true', default=argparse.SUPPRESS, help='Include symbols')
parser.add_argument("-c","--copy", action='store_true', default=argparse.SUPPRESS, help='Copy password to clipboard')

r = parser.parse_args()
length = int(r.length)
uppers = False
nums = False
symb = False

    #   Check for inserted arguments
if length < 8:
    length = 8
if 'uppers' in r:
    uppers = True
if 'nums' in r:
    nums = True
if 'symb' in r:
    symb = True

res = pass_gen(length, uppers, nums, symb)

    #   Printing
print("+---------------------------+")
print("| SECURE-PASSWORD-GENERATOR |")
print("+---------------------------+")

    #   Copy password to clipboard
if 'copy' in r:
    c.copy(res)
    print("Password copied!")

print(f"\nGenerated password: [{res}]")
