from dataclasses import dataclass
from genericpath import exists
from os import path, remove

def StrToCron(time:str):
    hour = time[:2]
    minute = time[3:]
    return (bool(int(minute[0]))*minute[0])+minute[1]+" "+(bool(int(hour[0]))*hour[0])+hour[1]

def schedShutdown(time:str):
    path = '/etc/cron.d/multimedia_off'
    with open(path,"r") as f:
        data = f.read()
    print(data)
    print(type(data))
    return
 