import re

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