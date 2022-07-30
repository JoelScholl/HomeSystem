import HomeSystem.audio as audio
import HomeSystem.hm as hm
import time
import builtins

def print(*args):
    input_str=''
    for strs in args:
        input_str+=' '+str(strs)
    builtins.print("["+time.asctime()+"]: "+input_str)

def soft_shutdown():
    if(audio.get_beast()):
        print("Shutting down Beast!")
        audio.set_beast()
        print("Beast killed.")

    if(audio.get_amp(0)):
        print("Shutting down Amp 1")
        audio.set_amp(0,False)

    if(audio.get_amp(1)):
        print("Shutting down Amp 2")
        audio.set_amp(1,False)

    if(audio.get_amp(2)):
        print("Shutting down Amp 3")
        audio.set_amp(2,False)

    time.sleep(15)
    print("Shutting down Torus!")
    audio.set_torus('off')

shutdown_time = hm.get_sysvar('49106')['value_text']
#auto_chk = True if (hm.get_sysvar('50807')['value_text']=='auto') else False
#time_chk = True if (((time.localtime()[3] == int(shutdown_time[0:2])) and (abs(time.localtime()[4]-int(shutdown_time[3:5]))<50))) else False
#master_chk = False if hm.get_state_val('5263','5293','5297') == 'true' else True
#beast_shutdown_time 49106 torus shutdown_time: 52798
#best_auto_manuel: 52847 torus_auto_manuel: 50807

auto_chk = True
time_chk = True
master_chk = True


print(shutdown_time,time.localtime()[3],time_chk,master_chk)

if(auto_chk and master_chk):
    print("Autocheck and Mastercheck passed!")
    if(time_chk or (time.localtime()[3]==1)):
        print("Timecheck passed, running soft shutdown")
        soft_shutdown()
