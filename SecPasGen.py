#!/usr/bin/env python3
import random as rd
import argparse
import re
import clipboard as c

    # Generating password! func
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
    for i in range(length):
        password += combine[rd.randint(0,len(combine)-1)]

    return password

    #check if password match given inputs(up_case,nums,symbols)  # if not generate another! func
def matched_pass(length, uppers, nums, symb):
    f = True
    password = pass_gen(length, uppers, nums, symb)
    if uppers:
        if not re.search(r"[A-Z]", password):
            f = False

    if nums:
        if not re.search(r"\d", password):
            f = False

    if symb:
        if not re.search(r"[!@#$%^&*]", password):
            f = False

    if f:
        return password
    else:
        return matched_pass(length, uppers, nums, symb)

    # Creating arguments
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

    # Check for inserted arguments
if length < 8:
    length = 8
if 'uppers' in r:
    uppers = True
if 'nums' in r:
    nums = True
if 'symb' in r:
    symb = True

res = matched_pass(length, uppers, nums, symb)

    #Printing
print("\n-------------------------")
print("SECURE-PASSWORD-GENERATOR")
print("-------------------------")

if 'copy' in r:
    c.copy(res)
    print("Password copied!")

print(f"\nGenerated password: [{res}]")

