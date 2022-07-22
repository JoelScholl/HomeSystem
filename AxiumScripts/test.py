import axiumctrl as ax
import requests as rq

#ax.chk_amp(0)
r = rq.get("http://192.168.1.32/Web/Handler.php?page=home&action=read",headers={},data={},timeout=3)
print(r)