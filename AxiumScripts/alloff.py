import HomeSystem as ax
import time

if(ax.chk_beast()):
	ax.kill_beast()

if(ax.chk_amp(0)):
	ax.amp(0,False)

if(ax.chk_amp(1)):
	ax.amp(1,False)

if(ax.chk_amp(2)):
	ax.amp(2,False)

shutdown_time = ax.get_sysvar('49106')
auto = ax.get.sysvar('50807')

ax.torus('off')
print("Torus off")
time.sleep(15)
#ax.torus('off')
print("Torus off")