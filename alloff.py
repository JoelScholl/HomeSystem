from HomeSystem import Axium as ax, HM
import time

# if(ax.chk_beast()):
# 	axium.kill_beast()

# if(ax.chk_amp(0)):
# 	ax.amp(0,False)

# if(ax.chk_amp(1)):
# 	ax.amp(1,False)

# if(ax.chk_amp(2)):
# 	ax.amp(2,False)

shutdown_time = ax.get_sysvar('49106')['value_text']
auto_chk = ax.get_sysvar('50807')['value_text']

#ax.torus('off')
print("Torus off")
time.sleep(15)
#ax.torus('off')
print("Torus off")