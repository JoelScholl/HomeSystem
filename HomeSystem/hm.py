import HomeSystem.www as www
import xml.etree.ElementTree as ET
import time
import builtins

def print(*args:str):
    input_str=''
    for strs in args:
        input_str+=' '+strs
    builtins.print("["+time.asctime()+"]: "+input_str)

def parse_xml(content:str):
    tree = ET.ElementTree(ET.fromstring(content.text))
    root = tree.getroot()
    return root

def call(cgi:str,params:str=''):
    hm_url = "http://192.168.1.41/addons/xmlapi/"+cgi+".cgi"+params
    print("Calling:",hm_url)
    response = www.get(hm_url,headers={},data={},timeout=10)
    if(response):
        return response

def get_sysvar(id:str):
    var_xml = call('sysvar','?ise_id='+id)
    var = parse_xml(var_xml)
    return var[0].attrib

def get_sysvarlist(arg:str=''):
    varlist_xml = call('sysvarlist',arg)
    varlist = parse_xml(varlist_xml)
    #for child in varlist:
    #	print(child.attrib)
    return varlist

def get_state(device_id:str, channel_id:str='', datapoint_id:str=''):
    state_xml = call('state','?device_id='+device_id+'&channel_id='+channel_id+'&datapoint_id='+datapoint_id)
    state = parse_xml(state_xml)
    return state

def get_state_val(device_id:str, channel_id:str='', datapoint_id:str=''):
    return get_state(device_id,channel_id,datapoint_id)[0].attrib['value']