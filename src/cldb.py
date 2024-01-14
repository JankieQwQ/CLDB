import sys
from syntax import syntax
welc = '''
CLDB - CELLO DEBUGGER

Usage:
    cldb [source file] [option]
Options:
    -s Syntax error check
    -l Monitor vital signs (heartbeat, SpO2)
'''

def main(argc:int = len(sys.argv),argv:list = sys.argv) -> int:
    if argc == 1:
        print(welc)
        return 0
    elif argc == 2:
        print('Invalid parameter.')
        return -1
    
    modelist = ['-s','-l']
    filename = argv[1]
    mode     = argv[2]
    syntaxer = Syntax(filename)
    if not mode in modelist:
        print('Invalid parameter.')
        return -1
    if mode == '-s':
        syntaxer.check()
        print('Success!')
    return 0

if __name__ == '__main__':
    code = main()
    raise SystemExit(code)