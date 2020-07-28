import sys

def mult(a, b):
    ''' This function returns a*b'''
    return a*b

if len(sys.argv) == 3:
    print(mult(float(sys.argv[1]), float(sys.argv[2])))