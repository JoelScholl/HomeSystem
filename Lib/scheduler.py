import os

def sudo(command):
    return os.system(f"sudo bash -c '{command}'")

def StrToCron(time:str):
    hour = time[:2]
    minute = time[3:]
    return (bool(int(minute[0]))*minute[0])+minute[1]+" "+(bool(int(hour[0]))*hour[0])+hour[1]

def schedShutdown(time:str):
    path = '/etc/cron.d/multimedia_off'
    cron_t = StrToCron(time)
    print(cron_t)
    cmd='printf "'+cron_t+' * * * root python3 /home/pi/HomeSystem/alloff.py >> /var/log/home.log 2>&1\n" > '+path
    print(cmd)
    return sudo(cmd)
    
