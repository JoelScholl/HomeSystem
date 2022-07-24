import requests

def get(url:str,headers = None, data = None, timeout:int = 3, loop:bool = False):
	while(loop):
		print("Looping")
		try:
			r = requests.get(url,headers=headers,data=data,timeout=timeout)
			return r
		except:
			continue
			#print("Except")
	r = requests.get(url,headers=headers,data=data,timeout=timeout)
	return r

def post(url:str,headers = None, data = None, timeout:int = 3, loop:bool = False):
	while(loop):
		#print("Looping")
		try:
			r = requests.post(url,headers=headers,data=data,timeout=timeout)
			return r
		except:
			continue
	print("Once with",url,headers,data,timeout)
	r = requests.post(url,headers=headers,data=data,timeout=timeout)
	#print("Done")
	return r	