from flask import Flask
from flask import request
from markupsafe import escape
import Lib.hm as hm
import Lib.audio as audio
from Lib.logging import print
from Lib.scheduler import *
import time
import json
import torusOff

### States ###
#tv = False

app = Flask(__name__)

#Manage torus_shutdown_time changes
@app.route('/')
def home():
    return '<h3>Currently only /sysvar is supported.</h3>'

#Catch stray routes
@app.route('/sysvar', methods=['GET'])
def sysvar():

    #Interpret request
    id = request.args.get('id')
    name = request.args.get('name')
    value = hm.VarToString(id,request.args.get('value'))
    print("ID:",id)
    print("Name:",name)
    print("Value:",value)

    #Switch to correct function
    if id=='52798':
        schedule('torusOff',value)
    if id=='60189':
        schedule('torusOn',value)
    if id=='49106':
        schedule('beastOff',value)
    
    return '<h3>ID: {}</h3><h3>Name: {}</h3><h3>Value: {}</h3>'.format(escape(id),escape(name),escape(value))

@app.route('/plex', methods=['POST'])
def plexhook():
        payload = json.loads(request.form.get('payload'))
        #This could cause potentially forceful takeover of speaker source if left playing in the background.
        if payload['Player']['uuid'] == '022f12ae-dae4-4196-a78e-ba31e7f9b634':
            if payload['event']=='media.play' or payload['event']=='media.resume':
                if(not audio.getTorus()):
                    audio.setTorus('on')
                    hm.setState('joelaux','true')
                    time.sleep(10)
                    audio.set('joel','on','multiroom','60')
                else:
                    hm.setState('joelaux','true')
                    audio.set('joel','on','multiroom','60')
        return '<h3></h3>'

@app.route('/torus_shutdown')
def run_soft_shutdown():
    torusOff.force_shutdown()
    return '<h3></h3>'


#Run Flask server upon running process
if __name__ == '__main__':
    app.run(debug=True,port=32800,host='192.168.1.44')