import HomeSystem.audio as audio
import HomeSystem.hm as hm
import time
import logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG)

def soft_shutdown():
    if(audio.get_beast()):
        print("Shutting down Beast!")
        audio.set_beast()
        logging.debug("Beast killed.")

    if(audio.get_amp(0)):
        print("Shutting down Amp 1")
        audio.set_amp(0,False)

    if(audio.get_amp(1)):
        print("Shutting down Amp 2")
        audio.set_amp(1,False)

    if(audio.get_amp(2)):
        print("Shutting down Amp 3")
        audio.set_amp(2,False)

shutdown_time = hm.get_sysvar('49106')['value_text']
auto_chk = True if (hm.get_sysvar('50807')['value_text']=='auto') else False
time_chk = True if (((time.localtime()[3] == int(shutdown_time[0:2])) and (abs(time.localtime()[4]-int(shutdown_time[3:5]))<10))) else False
master_chk = False if hm.get_state_val('5263','5293','5297') == 'true' else True

logging.debug("Shutdown Time is set to: "+str(shutdown_time))
logging.debug("Current time is: "+str(time.localtime()[3]))
logging.debug("Time check is thus: "+str(time_chk))
logging.debug("Master Check is "+str(master_chk))


if(auto_chk and master_chk):
    logging.debug("Autocheck and Mastercheck passed!")
    if(time_chk or (time.localtime()[3]==1)):
        logging.debug("Timecheck passed, running soft shutdown")
        soft_shutdown()
