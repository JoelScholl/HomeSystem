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

def main():
    joel_chk = False if (hm.getStateVal('stromjoel') == 'true') else True
    tv_chk = False if (hm.getStateVal('tv') == 'true') else True
    rkport_chk = False if (hm.getStateVal('rockports') == 'true') else True

    print("joel_chk",joel_chk,"tv_chk",tv_chk,"rkport_chk",rkport_chk)

    if(joel_chk and tv_chk and rkport_chk):
        print("All checks passed!")
        soft_shutdown()

    elif(time.localtime()[3]==1):
        print("Forcing shutdown at 1:00 am!")
        soft_shutdown()

if __name__== '__main__':
    main()
