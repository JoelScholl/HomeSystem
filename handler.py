from flask import Flask
from flask import request
from markupsafe import escape
import Lib.hm as hm
from Lib.logging import print
from Lib.scheduler import *

app = Flask(__name__)

#Manage torus_shutdown_time changes
@app.route('/sysvar')
def torus_shutdown_time():
    return '<h3>I choose you!</h3>'

#Catch stray routes
# @app.route('/sysvar', methods=['GET'])
# def mainroute():
#     id = request.args.get('id')
#     name = request.args.get('name')
#     value = hm.VarToString(id,request.args.get('value'))
#     print("ID:",id)
#     print("Name:",name)
#     print("Value:",value)
#     return '<h3>ID: {}</h3><h3>Name: {}</h3><h3>Value: {}</h3>'.format(escape(id),escape(name),escape(value))

