from asyncio.base_futures import _format_callbacks
import builtins
import HomeSystem.audio as audio
import HomeSystem.hm as hm
import xml.etree.ElementTree as ET
import time
import builtins

def print(*args):
    input_str=''
    for strs in args:
        input_str+=' '+str(strs)
    builtins.print("["+time.asctime()+"]: "+input_str)

#tv_chk = False if hm.get_state_val('5141','5173','5179') == 'true' else True
#rkport_chk = False if hm.get_state_val('5337','5379','5383') == 'true' else True

#print(tv_chk)
#print(rkport_chk)

# varlist = hm.get_sysvarlist()
# for childs in varlist:
#     builtins.print(childs)

from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

#Main route handles all
@app.route('/sysvar', methods=['GET'])
def update():
    id = request.args.get('id')
    name = request.args.get('name')
    value = request.args.get('value')
    builtins.print("ID:",id)
    builtins.print("Name:",name)
    builtins.print("Value:",value)
    return '<h3>ID: {}</h3><h3>Value: {}</h3>'.format(escape(id),escape(value))

#Run Flask server upon running process
if __name__ == '__main__':
    app.run(debug=True,port=50000,host='192.168.1.135')