import Lib.hm as hm
from Lib.www import get

def main():
    xml = get('http://192.168.1.45:8080/goform/formMainZone_MainZoneXmlStatusLite.xml')
    root = hm.parseXML(xml)
    state = root[0][0].text
    print(state)
    if(state=='ON'):
        print("Denon is running")
        print("Calling: hm.setState("+hm.deviceID('denon')[2]+",'true')")
        hm.setState('denon','true')
    elif(state=='OFF'):
        print("Denon isn't running")
        print("Calling: hm.setState("+hm.deviceID('denon')[2]+",'false')")
        hm.setState('denon','false')

if __name__ == '__main__':
    main()