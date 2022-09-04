import requests
from Lib.logging import print

def get(url:str,headers = None, data = None, timeout:int = 3, loop:bool = False,nmax:int = 10):
	while(loop and nmax>0):
		print("Looping")
		try:
			r = requests.get(url,headers=headers,data=data,timeout=timeout)
			print("Going twice with URL:"+url)
			return r
		except:
			print("Except")
			nmax-=1
			continue
			
	try:
		r = requests.get(url,headers=headers,data=data,timeout=timeout)
		print("Going once with URL:"+url)
		return r
	except:
		print("Webserver at "+url+"refused to connect.")
	

def post(url:str,headers = None, data = None, timeout:int = 3, loop:bool = False, nmax:int = 10):
	while(loop and nmax>0):
		print("Looping")
		try:
			r = requests.post(url,headers=headers,data=data,timeout=timeout)
			print("Going twice with URL:"+url)
			return r
		except:
			print("Except")
			nmax-=1
			continue
			
	try:
		r = requests.post(url,headers=headers,data=data,timeout=timeout)
		print("Going once with URL:"+url)
		return r
	except:
		print("Webserver at "+url+"refused to connect.")