import HomeSystem.audio as audio
import HomeSystem.wreq as wreq
import HomeSystem.hm as hm

Torus = hm.get_sysvar(id='50807')
varlist = hm.get_sysvarlist()
amp2 = audio.chk_amp()

print(Torus)
print(varlist)
print(amp2)
