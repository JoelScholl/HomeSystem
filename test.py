import builtins
import HomeSystem.audio as audio
import HomeSystem.hm as hm
import xml.etree.ElementTree as ET
import time
import builtins

def print(*args:str):
    input_str=''
    for strs in args:
        input_str+=' '+strs
    builtins.print("["+time.asctime()+"]: "+input_str)

print("This works","well")

# varlist = hm.get_sysvarlist()
# for childs in varlist:
#     builtins.print(childs)