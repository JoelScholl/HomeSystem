import HomeSystem.audio as audio
import HomeSystem.hm as hm


state = hm.get_state('5263','5293','5297')[0].attrib['value']
state2 = hm.get_state_val('5263','5293','5297')

print(state)
print(state2)
print(audio.get_amp(0))
print(audio.get_amp(1))
print(audio.get_amp(2))
print(audio.get_beast())
