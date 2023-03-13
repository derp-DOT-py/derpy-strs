'''some derpy string functions I wrote'''

import sys

B64STRS = [chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]+[chr(i) for i in range(48,58)]+["+","/"]
HEXSTRS = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']

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
    return ''.join([i for i in string if i.isdigit()])

def gethex(string):
    '''extract valid hex digits from a string'''
    return ''.join([i for i in string if i in HEXSTRS]).lower()


def isb36(string):
    '''true if string is a valid base36 string'''
    return (all([(i in [chr(j) for j in range(48,58)]+[chr(k) for k in range(65,91)]) for i in string])) or (all([(i in [chr(j) for j in range(48,58)]+[chr(k) for k in range(97,123)]) for i in string]))

def isb64(string):
    '''true if string is a valid base64 string'''
    return all([(i in B64STRS) for i in string])

def isdec(string):
    '''true if string.isdecimal(); ... (it's just a shorter alias)'''
    return string.isdecimal()

def ishex(string):
    '''true if string is a valid hexstring'''
    return all([(i in HEXSTRS) for i in string])




def main():
    print('test')

if __name__ == "__main__":
    main()
