import Lib.audio as audio
import Lib.hm as hm
from Lib.logging import print
import time

def soft_shutdown():
    if(audio.getBeast()):
        print("Shutting down Beast!")
        audio.setBeast()
        print("Beast killed.")

    if(audio.getAmp(0)):
        print("Shutting down Amp 1")
        audio.setAmp(0,False)

    if(audio.getAmp(1)):
        print("Shutting down Amp 2")
        audio.setAmp(1,False)

    if(audio.getAmp(2)):
        print("Shutting down Amp 3")
        audio.setAmp(2,False)

    time.sleep(15)
    print("Shutting down Torus!")
    audio.setTorus('off')

auto_chk = True if (hm.getSysVar('50807')['value_text']=='auto') else False
joel_chk = False if (hm.getStateVal('5263','5293','5297') == 'true') else True
tv_chk = False if (hm.getStateVal('5141','5173','5179') == 'true') else True
rkport_chk = False if (hm.getStateVal('5336','5379','5383') == 'true') else True

print("Auto_chk",auto_chk,"joel_chk",joel_chk,"tv_chk",tv_chk,"rkport_chk",rkport_chk)

def main():
    if(auto_chk and joel_chk and tv_chk and rkport_chk):
        print("All checks passed!")
        soft_shutdown()

    elif(time.localtime()[3]==1):
        print("Forcing shutdown at 1:00 am!")
        soft_shutdown()

main()
