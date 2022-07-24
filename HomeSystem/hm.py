import HomeSystem.www as www
import xml.etree.ElementTree as ET

def parse_xml(content:str):
    tree = ET.ElementTree(ET.fromstring(content.text))
    root = tree.getroot()
    return root

def call(cgi:str,params:str=''):
    hm_url = "http://192.168.1.41/addons/xmlapi/"+cgi+".cgi"+params
    response = www.get(hm_url,headers={},data={})
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