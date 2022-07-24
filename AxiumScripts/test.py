from HomeSystem import Axium as ax, HM
import xml.etree.ElementTree as ET

hm = HM()
sysvarlist = hm.get_sysvarlist()

print(sysvarlist)
for child in sysvarlist:
    print(child.keys)

    

