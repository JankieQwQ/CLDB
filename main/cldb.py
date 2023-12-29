import re
import sys

welc = '''
CLDB - CELLO DEBUGGER

Usage:
    cldb [source file] [option]
Options:
    -s Syntax error check
    -l Monitor vital signs (heartbeat, SpO2)
'''

class Syntax:
    def __init__(self, filename: str):
        with open(filename, 'r') as file:
            self.text = file.read()

    def check(self):
        text = re.sub(r'//.*|/\*.*?\*/', '', self.text, flags=re.DOTALL)
        module_pattern = r'\bmodule\s+(\w+)\s*\(.*?\)\s*;\s*endmodule\b'
        modules = re.findall(module_pattern, text)
        if not modules:
            raise RuntimeError('Unknown module.')
        
        port_pattern = r'\b(input|output|inout)\s+(\w+)(?!.*\))'
        ports = re.findall(port_pattern, text)
        if not ports:
            raise RuntimeError('Unknown port.')
        
        semicolon_pattern = r'(?<!endcase|endmodule|end)\s*;'
        if not re.search(semicolon_pattern, text):
            raise RuntimeError('Unfinished command.')
        
        variable_pattern = r'\b(reg|wire|integer|parameter)\s+(\[\d+:\d+\]\s*)?(\w+)(?!.*;)'
        variables = re.findall(variable_pattern, text)
        if not variables:
            raise RuntimeError('Unknown variable.')
        
        return 0

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