from enum import auto
import Lib.audio as audio
import Lib.hm as hm
from Lib.logging import print

auto_chk = True if (hm.getSysVar('52847')['value_text']=='auto') else False

print("Auto_Ch:",auto_chk)

def main():
    if(auto_chk):
        if(audio.getBeast()):
            print("Shutting down beast")
            audio.setBeast()
            print("Beast killed.")

main()