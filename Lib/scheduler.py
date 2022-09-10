import os
from Lib.logging import print

def sudo(command):
    return os.system(f"sudo bash -c '{command}'")

def StrToCron(time:str):
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    return minute+' '+hour

def schedule(script:str,value:str):
    path = '/etc/cron.d/'+script

    #Write empty cron file if set to manual
    if(value=='manuell'):
        cmd='printf "\n" > '+path
        
    #Else write cron job
    else:
        time = StrToCron(value)
        cmd='printf "'+time+' * * * root python3 /home/pi/HomeSystem/'+script+'.py >> /var/log/home.log 2>&1\n" > '+path
    print(cmd)
    return sudo(cmd)
    
