import HomeSystem.www as www

def send_cmd(payload):
        '''Takes Payload and sends command.'''
        id='3764335675'
        page = "http://192.168.1.58/axium.cgi?id="+id
        headers = {'Host': '192.168.1.58','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-axium','Content-Length': '8','Origin': 'http://192.168.1.58','Connection': 'keep-alive','Referer': 'http://192.168.1.58/zone.html?id=3764335675'}
        print("Posting!")
        www.post(page,headers=headers,data=payload,timeout=1)

class zone():
    def __init__(self, id):
        self.name = __name__
        self.id = id
        self.src = None
        self.vol = None
        self.Mute = None

    def update(self):
        return

def zone_id(zone:str):
    zone_dict = {'04':'04','4':'04','joel':'04',
                '06':'06','6':'06','joelbad':'06'}
    return zone_dict[zone]

def state_id(state:str):
    state_dict = {'0':'0','off':'0',
                '1':'1','on':'1'}
    return state_dict[state]

def src_id(src:str):
    src_dict = {'05':'05','5':'05','janine':'05','Musik Janine':'05', #Musik Janine: 5
                '06':'06','6':'06','oppo':'06','Oppo DVD':'06', #Oppo DVD: 06
                '08':'08','8':'08','tvjoel':'08','TV Joël':'08', #TV Joël: 08
                '09':'09','9':'09', 'Multiroom':'09', #Multiroom: 09
                '0A':'0A','A':'0A','Musik Marcel':'0A', #Musik Marcel:  0A
                '0B':'0B','B':'0B','wohnen':'0B','TV Wohnen':'0B', #TV Wohnen: 0B
                '21':'21','radio1':'21','iRadio 1':'21', #iRadio 1: 21
                '12':'12','radio1':'12','iRadio 2':'12' #iRadio 2: 12
                }
    return src_dict[src]


def set_zone(zone:str, state:str):
    payload = '01'+zone_id(zone)+'0'+state_id(state)+'\r\n'
    print(payload)
    send_cmd(payload)

def set_src(zone:str, src:str):
    payload = '03'+zone_id(zone)+src_id(src)+'\r\n'
    send_cmd(payload)

def set_vol(zone:str='4', vol:str='10'):
    payload = '04'+zone+vol+'\r\n'
    send_cmd(payload)

def get_beast():
    beast_url = "http://192.168.1.12/index.php"
    headers = {'Host':'192.168.1.31','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate','Connection':'keep-alive','Referer':'http://192.168.1.31/protect/power.htm','Upgrade-Insecure-Requests':'1','Authorization':'Basic YWRtaW46YXZy'}
    try:
        r = www.get(beast_url,headers=headers,data={},timeout=2)
        if(r.ok):
            print("Beast is runnng!")
            return True
    except:
    print("Beast is not running!")
        return False

def get_amp(amp:int):
    '''Takes an integer in  {0,1,2} and returns the on/off state of the Amp.'''
    if(int not in range(2)):
        print("Wrong input! Call 'get_amp' with an integer in {0,1,2}!")

    get_amp_url = "http://192.168.1.3"+str((2+2*amp))+"/Web/Handler.php?page=home&action=read"
    r = www.get(get_amp_url,headers={'Host':'192.168.1.32'},data={}, timeout=3,loop=True)
    state = int(r.text[-3])
    print("Amp at","http://192.168.1.3"+str((2+2*amp)),"is",f'{"On" if state else "Off"}')
    return bool(state)

def set_amp(amp:int,state:bool):
    func_amp_url = "http://192.168.1.3"+str((2+2*amp))+"/Web/Handler.php?page=home&action=write&name=cur-standby&value="+str(int(state))+"&r=0.666583746119017"
    r = www.get(func_amp_url,headers={},data={},timeout=1)
    print(r)

def set_beast():
    beast_off = "http://192.168.1.12/shared/taskmanager.php?task=system&cmd=stop"
    r = www.get(beast_off,headers={},data={},timeout=1)
    print(r)


def set_torus(state:str):
    torus_url = "http://192.168.1.31/protect/power.htm?power1="+state
    payload = {}
    headers = {'Host':'192.168.1.31','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0','Accept':'text/www,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate','Connection':'keep-alive','Referer':'http://192.168.1.31/protect/power.htm','Upgrade-Insecure-Requests':'1','Authorization':'Basic YWRtaW46YXZy'}
    r = www.get(torus_url,headers=headers,data=payload,timeout=3)
    print(r)
