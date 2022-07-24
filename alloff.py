import HomeSystem.audio as audio
import HomeSystem.hm as hm
import time

shutdown_time = hm.get_sysvar('49106')['value_text']
auto_chk = hm.get_sysvar('50807')['value_text']

time_chk = True if (((time.localtime()[3] == int(shutdown_time[0:2])) and (abs(time.localtime()[4]-int(shutdown_time[3:5]))<10))) else False

print(time_chk)

# if(audio.chk_beast()):
# 	axium.kill_beast()

# if(audio.chk_amp(0)):
# 	audio.amp(0,False)

# if(audio.chk_amp(1)):
# 	audio.amp(1,False)

# if(audio.chk_amp(2)):
# 	audio.amp(2,False)


# ax.torus('off')
# print("Torus off")
# time.sleep(15)
# ax.torus('off')
# print("Torus off")