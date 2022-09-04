from flask import Flask
from flask import request
from markupsafe import escape
import Lib.hm as hm
from Lib.logging import print
from Lib.scheduler import *

app = Flask(__name__)

#Main route handles all
@app.route('/sysvar', methods=['GET'])
def update():
    id = request.args.get('id')
    name = request.args.get('name')
    value = hm.VarToString(id,request.args.get('value'))
    print("ID:",id)
    print("Name:",name)
    print("Value:",value)
    return '<h3>ID: {}</h3><h3>Value: {}</h3>'.format(escape(id),escape(value))
