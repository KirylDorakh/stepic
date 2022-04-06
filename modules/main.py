import sys
import subprocess

# import my_module
# from my_module import *
from my_module import foo as my_foo

from my_module import foo

foo()

print(len(sys.argv))

subprocess.call(['python', '-h'])
