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
    hm_url = "http://192.168.1.41/addons/xmlapi/"+cgi+".cgi"+params
    print("Calling:",hm_url)
    response = www.get(hm_url,headers={},data={},timeout=10)
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

def getState(device_id:str, channel_id:str='', datapoint_id:str=''):
    state_xml = call('state','?device_id='+device_id+'&channel_id='+channel_id+'&datapoint_id='+datapoint_id)
    state = parseXML(state_xml)
    return state

def getStateVal(device_id:str, channel_id:str='', datapoint_id:str=''):
    return getState(device_id,channel_id,datapoint_id)[0].attrib['value']

def VarToString(id:str, index:str):
    var = getSysVar(id)
    value_list = var['value_list'].split(";")
    return value_list[int(index)]