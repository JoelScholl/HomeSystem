import builtins
import HomeSystem.audio as audio
import HomeSystem.hm as hm
import xml.etree.ElementTree as ET
import time
import builtins

def print(*args):
    input_str=''
    for strs in args:
        input_str+=' '+str(strs)
    builtins.print("["+time.asctime()+"]: "+input_str)

tv_chk = False if hm.get_state_val('5141','5173','5179') == 'true' else True
rkport_chk = False if hm.get_state_val('5337','5379','5383') == 'true' else True

print(tv_chk)
print(rkport_chk)

# varlist = hm.get_sysvarlist()
# for childs in varlist:
#     builtins.print(childs)