import Lib.audio as audio
import Lib.hm as hm
from Lib.logging import print

main():
    ppl_chk = hm.getSysVar('8177')['value']
    if(ppl_chk):
        print(audio.setTorus('on'))

if __name__== '__main__':
    main()