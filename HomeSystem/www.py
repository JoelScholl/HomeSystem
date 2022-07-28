import requests
import time
import builtins

def print(*args:str):
    input_str=''
    for strs in args:
        input_str+=' '+strs
    builtins.print("["+time.asctime()+"]: "+input_str)


def get(url:str,headers = None, data = None, timeout:int = 3, loop:bool = False):
	while(loop):
		print("Looping")
		try:
			r = requests.get(url,headers=headers,data=data,timeout=timeout)
			print("Going twice with URL:"+url)
			return r
		except:
			print("Except")
			continue
			
	try:
		r = requests.get(url,headers=headers,data=data,timeout=timeout)
		print("Going once with URL:"+url)
		return r
	except:
		print("Webserver at "+url+"refused to connect.")
	

def post(url:str,headers = None, data = None, timeout:int = 3, loop:bool = False):
	while(loop):
		#print("Looping")
		try:
			r = requests.post(url,headers=headers,data=data,timeout=timeout)
			return r
		except:
			continue
	#print("Once with",url,headers,data,timeout)
	r = requests.post(url,headers=headers,data=data,timeout=timeout)
	#print("Done")
	return r	