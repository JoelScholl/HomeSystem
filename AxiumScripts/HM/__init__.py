import HTML as html


def parse_xml(self,content:str):
    xml = ET.fromstring(content)
    return xml

def call(self,cgi:str,params:str=''):
    hm_url = "http://192.168.1.41/addons/xmlapi/"+cgi+".cgi"+params
    response = HTML.get(hm_url,headers={},data={})
    return response