import sys

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
    
    return 0

if __name__ == '__main__':
    code = main()
    raise SystemExit(code)