import Lib.audio as audio
from Lib.logging import print

def main():
    if(audio.getBeast()):
        print("Shutting down beast")
        audio.setBeast()
        print("Beast killed.")

if __name__== '__main__':
    main()