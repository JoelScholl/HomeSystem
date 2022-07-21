import requests

def send_cmd(payload):
	id='3764335675'
	page = "http://192.168.1.58/axium.cgi?id="+id
	headers = {'Host': '192.168.1.58','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-axium','Content-Length': '8','Origin': 'http://192.168.1.58','Connection': 'keep-alive','Referer': 'http://192.168.1.58/zone.html?id=3764335675'}
	r = requests.post(page,headers=headers,data=payload,timeout=1)

def zone(zone:str, state:str):
	payload = '01'+zone_id(zone)+'0'+state_id(state)+'\r\n'
	send_cmd(payload)

def src(zone:str, src:str):
	payload = '03'+zone_id(zone)+src_id(src)+'\r\n'
	send_cmd(payload)
	
	
def vol(zone='4', vol='10'):
	payload = '04'+zone+vol+'\r\n'
	send_cmd(payload)

def try_request(url,headers,data,timeout:int,loop:bool):
	return

def chk_beast():
	beast_url = "http://192.168.1.12/index.php"
	headers = {'Host':'192.168.1.31','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate','Connection':'keep-alive','Referer':'http://192.168.1.31/protect/power.htm','Upgrade-Insecure-Requests':'1','Authorization':'Basic YWRtaW46YXZy'}
	try:
		r = requests.get(beast_url,headers=headers,data={},timeout=1)
		if(r.ok):
			print("Beast is running!")
			return True
	except:
		print("Beast is not running!")
		return False

def chk_amp(amp:int):
	chk_amp_url = "http://192.168.1.3"+str((2+2*amp))+"/Web/Handler.php?page=home&action=read"
	r = requests.get(chk_amp_url,headers={},data={}, timeout=1)
	state = int(r.text[-3])
	print("Amp at","http://192.168.1.3"+str((2+2*amp)),"is",f'{"On" if state else "Off"}')
	return bool(state)

def amp(amp:int,state:bool):
	func_amp_url = "http://192.168.1.3"+str((2+2*amp))+"/Web/Handler.php?page=home&action=write&name=cur-standby&value="+str(int(state))+"&r=0.666583746119017"
	r = requests.get(func_amp_url,headers={},data={},timeout=1)
	
def kill_beast():
	beast_off = "http://192.168.1.12/shared/taskmanager.php?task=system&cmd=stop"
	r = requests.get(beast_off,headers={},data={},timeout=1)
	print("Killed it!")


def torus(state:str):
	torus_url = "http://192.168.1.31/protect/power.htm?power1="+state
	payload = {}
	headers = {'Host':'192.168.1.31','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate','Connection':'keep-alive','Referer':'http://192.168.1.31/protect/power.htm','Upgrade-Insecure-Requests':'1','Authorization':'Basic YWRtaW46YXZy'}
	r = requests.get(torus_url,headers=headers,data=payload,timeout=3)
