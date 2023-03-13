'''some derpy string functions I wrote'''

import sys

DECIMALS = [chr(i) for i in range(48,58)]
LOWERS = [chr(i) for i in range(97,123)]
UPPERS = [chr(i) for i in range(65,91)]
B64STRS = UPPERS + LOWERS + DECIMALS + ["+","/"]
HEXSTRS = DECIMALS + UPPERS[:6] + LOWERS[:6]


def getalnum(string):
    '''extract alphanumerics from a string; (usually) good for generating base64 strings'''
    return ''.join([i for i in string if i.isalnum()])

def getalpha(string):
    '''extract alphabeticals from a sting; (usually) good for generating base36 (in conjunction with getdec)'''
    return ''.join([i for i in string if i.isalpha()])


def getb64(string):
    '''extract a valid base64 string (guaranteed, for when getalnum isn't good enough)'''
    return ''.join([i for i in string if i in B64STRS])

def getdec(string):
    '''extract decimals from a string'''
    return ''.join([i for i in string if i in DECIMALS])

def gethex(string):
    '''extract valid hex digits from a string'''
    return ''.join([i for i in string if i in HEXSTRS]).lower()

def getlowers(string):
    '''extract lower case letters from a string'''
    return ''.join([i for i in string if i in LOWERS])

def getuppers(string):
    '''extract upper case letters from a string'''
    return ''.join([i for i in string if i in UPPERS])

def rev(string):
    '''reverse a string'''
    return string[::-1]




def isb36(string):
    '''true if string is a valid base36 string'''
    return (all([(i in DECIMALS + UPPERS) for i in string])) or (all([(i in DECIMALS + LOWERS) for i in string]))

def isb64(string):
    '''true if string is a valid base64 string'''
    return all([(i in B64STRS) for i in string])

def isdec(string):
    '''true if string.isdecimal(); ... (it's just a shorter alias)'''
    return string.isdecimal()

def ishex(string):
    '''true if string is a valid hexstring'''
    return all([(i in HEXSTRS) for i in string])




def hxconv(string):
    '''a hex algorithm'''
    s = ''.join(getdec(string))
    hex_str = hex(int(s))[2:]
    if len(hex_str) == 1:
        return hex_str
    if all(char in 'abcdef' for char in hex_str):
        return hex_str
    return hex_str + hxconv(hex_str)



def main():
    print('test')

if __name__ == "__main__":
    main()
