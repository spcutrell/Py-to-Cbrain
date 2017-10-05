#!/usr/bin/env python3

import sys

def get_instructions(bf_code):
    valid_instr = {'>','<','+','-','.',',','[',']'}
    return [c for c in bf_code if c in valid_instr]

def get_body(instr):
    body = '\nunsigned int result_arr[MAX] = {0};\n' \
           'unsigned int *ptr = result_arr;'
    for c in instr:
        body += '\n'
        if c == '>':
           body += '++ptr;' 
        elif c == '<':
           body += '--ptr;' 
        elif c == '+':
            body += '++*ptr;'
        elif c == '-':
            body += '--*ptr;'
        elif c == '.':
            body += 'putchar(*ptr);'
        elif c == ',':
            body += '*ptr = getchar();'
        elif c == '[':
            body += 'while(*ptr) {'
        elif c == ']':
            body += '}'
    return body

def gather_c_file(instr):
    c_includes = "#include <stdio.h>"
    c_defines = "\n#define MAX 30000"
    c_main = "\nint main(void)\n{"
    c_body = get_body(instr)
    c_close = "\nreturn 0;\n}"
    final = c_includes + c_defines + c_main + c_body + c_close
    return final

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
    instr = get_instructions(data)

    with open("cbrain.c", 'w') as f:
        f.write(gather_c_file(instr))

if __name__ == "__main__":
    main()
