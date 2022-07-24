import HomeSystem.audio as audio
import HomeSystem.hm as hm


varlist = hm.get_sysvarlist()

for child in varlist:
    print(child.attrib)