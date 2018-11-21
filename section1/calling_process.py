import os
import sys

program = 'python'
print("Process calling")
arguments = ['called_process.py']

os.execvp(program, (program, ) + tuple(arguments))