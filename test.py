import builtins
import HomeSystem.audio as audio
import HomeSystem.hm as hm
import xml.etree.ElementTree as ET
import time

def print(input:str):
    builtins.print("["+time.asctime()+"]: "+input)

print("test")