import sys
from syntax import Syntax

welc = '''
CLDB - CELLO DEBUGGER

Usage:
    cldb [source file] [option]
Options:
    -s Syntax error check
    -l Monitor vital signs (heartbeat, SpO2)
'''

def main(argc=len(sys.argv), argv=sys.argv) -> int:
    if argc == 1:
        print(welc)
        return 0
    elif argc == 2:
        print('Invalid parameter.')
        return -1
    
    modelist = ['-s', '-l']
    filename, mode = argv[1:3]
    syntaxer = Syntax(filename)
    
    if mode not in modelist:
        print('Invalid parameter.')
        return -1
    
    if mode == '-s':
        syntaxer.check()
        print('Success!')
    
    return 0

if __name__ == '__main__':
    code = main()
    raise SystemExit(code)