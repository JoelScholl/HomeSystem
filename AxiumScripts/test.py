from HomeSystem import Axium, HM
import xml.etree.ElementTree as ET

hm = HM()
sysvarlist = hm.getsysvarlist()

print(sysvarlist)
print(ET.tostringlist(sysvarlist))

