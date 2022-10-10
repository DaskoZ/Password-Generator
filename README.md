
# Secure Password Generator

## Script to generate secure password using python!

## It can generate random password based on given arguments
## Requirements:
- python3
- clipboard
## Usage:

Lower-case letters included by default.
```usage
positional arguments:
  length        Password length[min='8']

optional arguments:
  -h, --help    show this help message and exit
  -u, --uppers  Include upper-case letters
  -n, --nums    Include numbers
  -sy, --symb   Include symbols
  -c, --copy    Copy password to clipboard
```

### Example:
Generate password with a length of 16 lower-case letters, upper-case letters, numbers, symbols and copying it to clipboard.

`python SecPasGen.py 16 -u -n -sy -c`

output:
```
-------------------------
SECURE-PASSWORD-GENERATOR
-------------------------

Password copied!
Generated password: [L8gNNOiP4Npd$xzS]
```
Generate password with a length of 8 letters and symbols.

`python SecPasGen.py 8 -u -sy`

output:
```
-------------------------
SECURE-PASSWORD-GENERATOR
-------------------------

Generated password: [@hmMvFYi]
```
