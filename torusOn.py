import Lib.audio as audio
import Lib.hm as hm
from Lib.logging import print

def main():
    ppl_chk = hm.getSysVar('8177')['value']=='true'
    print("People check has value:",ppl_chk)
    if(ppl_chk):
        print('Passed ppl_chk, value is ',ppl_chk)
        print("Response after turning on torus:",audio.setTorus('on'))

if __name__== '__main__':
    main()
