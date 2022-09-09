from flask import Flask
from flask import request
from markupsafe import escape
import Lib.hm as hm
from Lib.logging import print
from Lib.scheduler import *

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
    if id=='49106':
        schedule('beastOff',value)

    return '<h3>ID: {}</h3><h3>Name: {}</h3><h3>Value: {}</h3>'.format(escape(id),escape(name),escape(value))

@app.route('/plex')
def plexhook():
    with open('home/pi/HomeSystem/PlexLog.log','w') as f:
        f.write(request.data)
    return "hi"
