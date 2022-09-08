#import builtins
import Lib.audio as audio
#import Lib.hm as hm
#from Lib.logging import print
import xml.etree.ElementTree as ET
import time
import builtins
from Lib.scheduler import *
import json

from flask import Flask
from flask import request
from markupsafe import escape
app = Flask(__name__)
#Main route handles all
@app.route('/plex', methods=['POST'])
def update():
    payload = json.loads(request.form.get('payload'))
    print(payload)
    print(payload['Player']['uuid'],payload['event'])
    if payload['Player']['uuid'] == '022f12ae-dae4-4196-a78e-ba31e7f9b634' and (payload['event']=='media.play' or payload['event']=='media.resume'):
        print('Turning on speakers')
        audio.set('joel','on','multiroom','60')
    return '<h3>ID</h3>'

#Run Flask server upon running process
if __name__ == '__main__':
    app.run(debug=True,port=50000,host='192.168.1.44')

#http://192.168.0.184:50000/sysvar?id=time&value=1700

## Homematic Script
# string url= "http://192.168.178.200/anaus.php";
# if ( (dom.GetObject(ID_DATAPOINTS)).Get("CUxD.CUX2801001:1.CMD_EXEC")) {
#     (dom.GetObject(ID_DATAPOINTS)).Get("CUxD.CUX2801001:1.CMD_EXEC").State("curl -s -k " url);
# }
# else {
#     WriteLine("Datenpunkt nicht vorhanden");
# }