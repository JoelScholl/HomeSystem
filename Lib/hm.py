import Lib.www as www
from Lib.logging import print
import xml.etree.ElementTree as ET
import time
import builtins

def parseXML(content:str):
    tree = ET.ElementTree(ET.fromstring(content.text))
    root = tree.getroot()
    return root

def call(cgi:str,params:str=''):
    url = "http://192.168.1.41/addons/xmlapi/"+cgi+".cgi"+params
    print("Calling:",url)
    response = www.get(url,headers={},data={},timeout=10)
    if(response):
        return response

def getSysVar(id:str):
    var_xml = call('sysvar','?ise_id='+id)
    var = parseXML(var_xml)
    return var[0].attrib

def getSysVarList(arg:str=''):
    varlist_xml = call('sysvarlist',arg)
    varlist = parseXML(varlist_xml)
    #for child in varlist:
    #	print(child.attrib)
    return varlist

def deviceID(device:str):
    print(device)
    id = {'stromjoel':('5263','5293','5297'),
          'joelaux':('2735','2760','2764'),
          'tv':('5263','5293','5297'),
          'rockports':('5336','5379','5383')
          }
    return id[device]

def setState(device:str,value:str):
    id = deviceID(device)[2]
    r = call('statechange','?ise_id='+id+'&new_value='+value)
    return r

def getState(device:str):
    device_id, channel_id, datapoint_id = deviceID(device)
    state_xml = call('state','?device_id='+device_id+'&channel_id='+channel_id+'&datapoint_id='+datapoint_id)
    state = parseXML(state_xml)
    return state

def getStateVal(device:str):
    return getState(device)[0].attrib['value']

def VarToString(id:str, index:str):
    var = getSysVar(id)
    value_list = var['value_list'].split(";")
    return value_list[int(index)]
