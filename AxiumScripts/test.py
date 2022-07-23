import axiumctrl as ax
import axiumctrl.hm as hm
import xml.etree.ElementTree as ET

sysvarlist = hm.get.sysvarlist()
print(ET.tostringlist(sysvarlist))

