import os
from Lib.logging import print

def sudo(command):
    return os.system(f"sudo bash -c '{command}'")

def StrToCron(time:str):
    hour = time.split(':')[0].lstrip('0')
    minute = time.split(':')[1].lstrip('0')
    print(minute+' '+hour)
    return minute+' '+hour

def schedule(script:str,time:str):
    path = '/etc/cron.d/'+script
    cron_t = StrToCron(time)
    cmd='printf "'+cron_t+' * * * root python3 /home/pi/HomeSystem/'+script+'.py >> /var/log/home.log 2>&1\n" > '+path
    print(cmd)
    return sudo(cmd)
    
