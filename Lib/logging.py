#Imports
import builtins
import time

#Redefining print for logging purposes
def print(*args):
    input_str=''
    for strs in args:
        input_str+=' '+str(strs)
    builtins.print("["+time.asctime()+"]: "+input_str)

def log(*args):
   return