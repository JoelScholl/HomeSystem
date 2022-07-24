import HomeSystem.audio as audio
import HomeSystem.hm as hm
import time

shutdown_time = hm.get_sysvar('49106')['value_text']
auto_chk = hm.get_sysvar('50807')['value_text']
time_chk = True if (((time.localtime()[3] == int(shutdown_time[0:2])) and (abs(time.localtime()[4]-int(shutdown_time[3:5]))<10))) else False
master_chk = False if hm.get_state_val('5263','5293','5297') == 'true' else True

#if(master_chk):
if(audio.get_beast()):
    print("Shutting down Beast!")
    audio.set_beast()

if(audio.get_amp(0)):
    print("Shutting down Amp 1")
    audio.set_amp(0,False)

if(audio.get_amp(1)):
    print("Shutting down Amp 2")
    audio.set_amp(1,False)

if(audio.get_amp(2)):
    print("Shutting down Amp 3")
    audio.set_amp(2,False)

for i in range(20):
    print("Second: ",i)
    audio.get_amp(0)
    audio.get_amp(1)
    audio.get_amp(2)
    audio.get_beast()
    time.sleep(1)


# print("Torus off")
# time.sleep(10)
# ax.torus('off')
# print("Torus off")