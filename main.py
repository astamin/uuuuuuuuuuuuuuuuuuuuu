try :
    import requests , datetime , json , os , random , string , asyncio
    from queue import Queue
    from colorama import Fore , init 
    from time import sleep
    from concurrent.futures import ThreadPoolExecutor
    import ctypes
    import threading
    from queue import Queue
    import time
    import httpx
except :
    import os
    os.system('pip install -r re.txt')
import requests , datetime , json , os , random , string
from queue import Queue
from colorama import Fore , init 
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import ctypes
import threading
from queue import Queue
from fake_useragent import UserAgent
TITLE = ctypes.windll.kernel32.SetConsoleTitleW
result_queue = Queue()
init(autoreset=True)
Claimer = False
with open('config.json' , 'r') as file :
    config = json.load(file)
Name = ""
Bio = ""
webhook =""
Proxies = []
ConsoleLogo = f"{Fore.MAGENTA}<{Fore.CYAN} AsV {Fore.MAGENTA}>{Fore.RESET}"
TITLE('AsV V1')
def LoadSettings(config):
    global Name , Bio , webhook
    Name = config['Name']
    Bio = config['Bio']
    webhook = config['webhook']
    print(f"{ConsoleLogo} Load settings !")
    os.system('cls || clear')
def GetProxies():
    url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    response = requests.get(url=url).text
    with open('proxies.txt' , 'w') as file :
        file.write(response)

    Proxy = open('proxies.txt' , 'r').readlines()
    for Prox in Proxy :
        P = Prox.replace('\n' , " ")
        Proxies.append(P)
    os.remove('proxies.txt')
    print(f"{ConsoleLogo} Done Import {len(Proxies)} proxy !")
    os.system('cls || clear')
def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))
def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result
def generateUSER_AGENT():
            Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
            DPIs = [
                '480', '320', '640', '515', '120', '160', '240', '800'
            ]
            randResolution = random.randrange(2, 9) * 180
            lowerResolution = randResolution - 180
            DEVICE_SETTINTS = {
                'system': "Android",
                'Host': "Instagram",
                'manufacturer': f'{random.choice(Devices_menu)}',
                'model': f'{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}',
                'android_version': random.randint(18, 25),
                'android_release': f'{random.randint(1, 7)}.{random.randint(0, 7)}',
                "cpu": f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
                'resolution': f'{randResolution}x{lowerResolution}',
                'randomL': f"{RandomString(6)}",
                'dpi': f"{random.choice(DPIs)}"
            }
            return '{Host} 155.0.0.37.107 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(
                **DEVICE_SETTINTS)
async def UserChecker(username):
    pp = random.choice(Proxies)
    proxy = {
                 "http://":"http://{}".format(pp),
            }
    
    async with httpx.AsyncClient(proxies=proxy , timeout=4) as client :
        cookies = await client.get('https://www.instagram.com')
        csrftoken = cookies.cookies.get('csrftoken')
        headers = {
                        "Accept": "*/*",
                        "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Cookie": "massing",
                        "Dpr": "0.9",
                        "Origin": "https://www.instagram.com",
                        "Referer": "https://www.instagram.com/{}/".format(username),
                        "Sec-Ch-Prefers-Color-Scheme": "light",
                        "Sec-Ch-Ua": """Not_A Brand"";v=""8"", ""Chromium"";v=""120"", ""Google Chrome"";v=""120""",
                        "Sec-Ch-Ua-Mobile": "?0",
                        "Sec-Ch-Ua-Model": """""",
                        "Sec-Ch-Ua-Platform": """Windows""",
                        "Sec-Ch-Ua-Platform-Version": """10.0.0""",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                        "Viewport-Width": "238",
                        "X-Asbd-Id": "129477",
                        "X-Csrftoken": csrftoken,
                        "X-Fb-Friendly-Name": "PolarisBarcelonaProfileBadgeQuery",
                        "X-Fb-Lsd": "8zU6-6taj5nvCF19VJuRmo",
                        "X-Ig-App-Id": "936619743392459"}
        data = f'av=17841464245050085&__d=www&__user=0&__a=1&__req=3&__hs=19748.HYP%3Ainstagram_web_pkg.2.1..0.1&dpr=1&__ccg=UNKNOWN&__rev=1011051482&__s=wlmtlh%3Axkto79%3Az658jf&__hsi=7328560169802750276&__dyn=7xeUjG1mxu1syUbFp60DU98nwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO2O1Vw8G1nzUO0n24oaEd86a3a1YwBgao6C0Mo2sx-0z8-U2zxe2GewGwso88cobEaU2eUlwhEe87q7U88138bpEbUGdG1QwTwFwIw8O321LwTwKG1pg661pwr86C1mwrd6goK68jxeUnAw&__csr=gkML4vcLN2mBRpyqCSmQBBQozihkCbGlV9LAAy9aA8KVVEkzkqeh4F99VEiEECRgJ2pbBiExbhdfKEC4bhryVVdmGAKF8gyk8yqDDCXBBDwHJ0zx26801bSi029k02YS064o2l4iezzk09sCw2P-1te3a226Eb80xl0Hc0_816yw9-00FIE&__comet_req=7&fb_dtsg=NAcOTRjvM-fXT1VlxZ6oSOgcLDQj-48bLcaTuf9bxw8zdjeIHvAsRMA%3A17843691127146670%3A1706313365&jazoest=26312&lsd=8zU6-6taj5nvCF19VJuRmo&__spin_r=1011051482&__spin_b=trunk&__spin_t=1706313381&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisBarcelonaProfileBadgeQuery&variables=%7B%22username%22%3A%22{username}%22%7D&server_timestamps=true&doc_id=6887760227926196'
        try :
            response = await client.post(url='https://www.instagram.com/api/graphql' , headers=headers, data=data)
            if response.text.__contains__('id'):
                return False
            else :
                return True
        except :
             Proxies.remove(pp)

def UsernameChecks(username ):
            pp = random.choice(Proxies)
            proxy = {
                 "http://":"http://{}".format(pp),
            }
            try:
                headers = {
                        "Accept": "*/*",
                        "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Cookie": "massing",
                        "Dpr": "0.9",
                        "Origin": "https://www.instagram.com",
                        "Referer": "https://www.instagram.com/{}/".format(username),
                        "Sec-Ch-Prefers-Color-Scheme": "light",
                        "Sec-Ch-Ua": """Not_A Brand"";v=""8"", ""Chromium"";v=""120"", ""Google Chrome"";v=""120""",
                        "Sec-Ch-Ua-Mobile": "?0",
                        "Sec-Ch-Ua-Model": """""",
                        "Sec-Ch-Ua-Platform": """Windows""",
                        "Sec-Ch-Ua-Platform-Version": """10.0.0""",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                        "Viewport-Width": "238",
                        "X-Asbd-Id": "129477",
                        "X-Csrftoken": "dr120O7qrtRWYqNpve1ZKZMUUvabvmwX",
                        "X-Fb-Friendly-Name": "PolarisBarcelonaProfileBadgeQuery",
                        "X-Fb-Lsd": "8zU6-6taj5nvCF19VJuRmo",
                        "X-Ig-App-Id": "936619743392459"}
                data = f'av=17841464245050085&__d=www&__user=0&__a=1&__req=3&__hs=19748.HYP%3Ainstagram_web_pkg.2.1..0.1&dpr=1&__ccg=UNKNOWN&__rev=1011051482&__s=wlmtlh%3Axkto79%3Az658jf&__hsi=7328560169802750276&__dyn=7xeUjG1mxu1syUbFp60DU98nwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO2O1Vw8G1nzUO0n24oaEd86a3a1YwBgao6C0Mo2sx-0z8-U2zxe2GewGwso88cobEaU2eUlwhEe87q7U88138bpEbUGdG1QwTwFwIw8O321LwTwKG1pg661pwr86C1mwrd6goK68jxeUnAw&__csr=gkML4vcLN2mBRpyqCSmQBBQozihkCbGlV9LAAy9aA8KVVEkzkqeh4F99VEiEECRgJ2pbBiExbhdfKEC4bhryVVdmGAKF8gyk8yqDDCXBBDwHJ0zx26801bSi029k02YS064o2l4iezzk09sCw2P-1te3a226Eb80xl0Hc0_816yw9-00FIE&__comet_req=7&fb_dtsg=NAcOTRjvM-fXT1VlxZ6oSOgcLDQj-48bLcaTuf9bxw8zdjeIHvAsRMA%3A17843691127146670%3A1706313365&jazoest=26312&lsd=8zU6-6taj5nvCF19VJuRmo&__spin_r=1011051482&__spin_b=trunk&__spin_t=1706313381&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisBarcelonaProfileBadgeQuery&variables=%7B%22username%22%3A%22{username}%22%7D&server_timestamps=true&doc_id=6887760227926196'
                response = requests.post("https://www.instagram.com/api/graphql", headers=headers, data=data,proxies=proxy,timeout=3)
                if response.text.__contains__("id"):
                    return False
                else :
                    return True
            except Exception as F :
                 Proxies.remove(pp)
                 return False           

async def ExtractInfo(session):
    pp = random.choice(Proxies)
    proxy = {
                 "http://":"http://{}".format(pp),
            }
    async with httpx.AsyncClient(proxies=proxy , timeout=4) as client :
        cookies = await client.get('https://www.instagram.com')
        csrftoken = cookies.cookies.get('csrftoken')
        url = "https://www.instagram.com/api/v1/accounts/edit/web_form_data/"
        header = {}
        header['User-Agent'] = generateUSER_AGENT()
        header['Host'] = 'i.instagram.com'
        header['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        header['x-csrftoken'] = csrftoken
        header['cookie'] = f"csrftoken={csrftoken};sessionid={session}"
        cookis = {
            'csrftoken' : csrftoken ,
            'sessionid' : session
            }
        try :
            response = await client.get(url=url , headers=header , cookies=cookis)
            email = response.json()['form_data']['email']
            phone = response.json()['form_data']['phone_number']
            settings = {
                'email' : email ,
                'phone' : phone ,
                'session' :session
            }
            if os.path.exists('set.json') : os.remove('set.json')
            with open('set.json' , 'a') as file :
                json.dump(settings , file , indent=4)
            return True
        except :
            print(f'{ConsoleLogo} Session is burned !')
            exit()

def sessionextreact(session):
    csrfToken = requests.get('https://www.instagram.com').cookies.get('csrftoken')
    url = "https://www.instagram.com/api/v1/accounts/edit/web_form_data/"
    header = {}
    header['User-Agent'] = generateUSER_AGENT()
    header['Host'] = 'i.instagram.com'
    header['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    header['x-csrftoken'] = csrfToken
    header['cookie'] = f"csrftoken={csrfToken};sessionid={session}"
    cookies = {
         'csrftoken' : csrfToken ,
         'sessionid' : session
         
    }
    try :
        response = requests.get(url=url , headers=header ,cookies=cookies)
        email = response.json()['form_data']['email']
        phone = response.json()['form_data']['phone_number']
        setting = {
             'email' : email ,
             'phone'  : phone ,
             'session' : session
        }
        if os.path.exists('set.json'): os.remove('set.json')
        with open('set.json' , 'a') as file :
             json.dump(setting , file)
        return True
    except :
        print(f"{ConsoleLogo} Session was Burned!")
        exit()

async def Claime(target):
    pp = random.choice(Proxies)
    proxy = {
                 "http://":"http://{}".format(pp),
            }
    with open('set.json' , 'r') as file :
         setting = json.load(file)
    email = setting['email']
    phone = setting['phone']
    session = setting['session']
    async with httpx.AsyncClient(proxies=proxy , timeout=4) as client :
        cookies = await client.get('https://www.instagram.com')
        csrftoken = cookies.cookies.get('csrftoken')
        cooki = {
        'csrftoken': csrftoken,
        'sessionid': session,
        }
        headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '1.5',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/edit/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.129", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'viewport-width': '751',
        'x-asbd-id': '129477',
        'x-csrftoken': csrftoken,
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3VA9irkEV7dofWrMv8XXLS9QYrPMGjm3cSc4rXc7OIU2EC',
        'x-instagram-ajax': '1012232105',
        'x-requested-with': 'XMLHttpRequest',}

        data = {
            "biography" : Bio ,
            'chaining_enabled': 'on',
            'email': email,
            'external_url': 'https://www.instagram.com/powerfulllasta',
            'first_name': '',
            'phone_number': phone,
            'username': target,

        }
        try :
            response = await client.post(url='https://www.instagram.com/api/v1/web/accounts/edit/' , headers=headers ,data=data , cookies=cooki)
            if response.status_code == 200 and response.text.__contains__('ok'):
                timer = datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
                with open('claims.txt' , 'a') as file :
                     file.write(f'\n@{target} \nClaimed : {timer}')
                return True
            else :
                print(f'{ConsoleLogo} @{target} error to claim it -> {Fore.RED}{response.text}{Fore.RESET}')
                with open('claims.txt' , 'a') as file :
                     file.write(f"\n@{target} error to claim -> {response.text}")
        except :
            print(f'{ConsoleLogo} @{target} error to claim it -> {Fore.RED}{response.status_code}{Fore.RESET}')
            with open('claims.txt' , 'a') as file :
                     file.write(f"\n@{target} error to claim -> {response.text}")
def Console(Att , target , rs):
    print(f"{Fore.CYAN} Attempts : {Att} \n{Fore.MAGENTA} Target : @{target}\n{Fore.YELLOW}R/S : {rs}{Fore.RESET}")

def Send(username):
        lines =open('claims.txt' , 'r').readlines()
        for line in lines :
            if "Claim" in line :
             timeofclaim = line.split('Claimed :')[0]
             if 'Claim' in timeofclaim :
                  timeofclaim = timeofclaim.replace("Claimed :" , " ")
        payload = {
        "username": Name,
        "avatar_url": "https://i.pinimg.com/564x/21/d6/7f/21d67f1d6b3be5bb2e39395311c77fc6.jpg",
        "embeds": [
            {
                "title": "",
                "description": f"{Bio}, [@{username}](https://www.instagram.com/{username})",
                "footer": {
                    "text": timeofclaim
                }
            }
        ]
    }
        json_payload = json.dumps(payload)
        response = requests.post(webhook, data=json_payload, headers={"Content-Type": "application/json"})

def main():
    LoadSettings(config)
    GetProxies()
    os.system('cls || clear')
    TITLE('AsV Registry !')
    Threads = int(input(f'{ConsoleLogo} Enter Threads : '))
    session = input(f'{ConsoleLogo} Enter Session : ')
    result = asyncio.run(ExtractInfo(session))
    if os.path.exists('targets.txt') is False:
        print(f"{ConsoleLogo} No target File Found!")
        exit()
    attempts = 0
    while True :
        starttime = time.time()
        rs  = 0
        usernames = open('targets.txt' , 'r').readlines()
        target = random.choice(usernames)
        response = asyncio.run(UserChecker(target))
        rs += 1
        if response is False :
            attempts +=1
        elif response is True :
            respon = asyncio.run(Claime(target))
            if respon is True :
                Send(target)
                claimtime = datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
                print(f"{Fore.CYAN}@{target} \n{Fore.BLUE}Attempt -> {attempts}\n{Fore.MAGENTA}Claimed At -> {claimtime}{Fore.RESET}")
                input('Enter to exit : ')
                exit()
            else :
                pass
        elapsed = time.time() - starttime
        Console(attempts , target , rs)
        os.system('cls || clear')
        if elapsed >= 1 :
            TITLE(f'Asv $ At -> {attempts} $ R/S -> {rs}')
            rs = 0
                 
main()