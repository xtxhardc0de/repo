import os, threading, colorama, requests, ctypes
from urllib.parse import unquote
from bs4 import BeautifulSoup

def colors_load():
    global blue, light_blue, red, light_red, yellow, light_yellow, magenta, light_magenta, reset_color, green, light_green
    blue = colorama.Fore.BLUE
    light_blue = colorama.Fore.LIGHTBLUE_EX
    red = colorama.Fore.RED
    light_red = colorama.Fore.LIGHTRED_EX
    yellow = colorama.Fore.YELLOW
    light_yellow = colorama.Fore.LIGHTYELLOW_EX
    magenta = colorama.Fore.MAGENTA
    light_magenta = colorama.Fore.LIGHTMAGENTA_EX
    reset_color = colorama.Fore.RESET
    green = colorama.Fore.GREEN
    light_green = colorama.Fore.LIGHTGREEN_EX

def banner_update():
    os.system('cls')
    banner = f"""{light_blue}
██{light_yellow}╗{light_blue}     ██████{light_yellow}╗{light_blue}      █████{light_yellow}╗{light_blue} ██{light_yellow}╗{light_blue} ██████{light_yellow}╗{light_blue} 
██{light_yellow}║{light_blue}     ██{light_yellow}╔══{light_blue}██{light_yellow}╗ {light_blue}   ██{light_yellow}╔══{light_blue}██{light_yellow}╗{light_blue}██{light_yellow}║{light_blue}██{light_yellow}╔═══{light_blue}██{light_yellow}╗{light_blue}
██{light_yellow}║  {light_blue}   ██████{light_yellow}╔╝{light_blue}    ███████{light_yellow}║{light_blue}██{light_yellow}║{light_blue}██{light_yellow}║  {light_blue} ██{light_yellow}║{light_blue}
██{light_yellow}║  {light_blue}   ██{light_yellow}╔══{light_blue}██{light_yellow}╗    {light_blue}██{light_yellow}╔══{light_blue}██{light_yellow}║{light_blue}██{light_yellow}║{light_blue}██{light_yellow}║   {light_blue}██{light_yellow}║{light_blue}
███████{light_yellow}╗{light_blue}██{light_yellow}║{light_blue}  ██{light_yellow}║ {light_blue}   ██{light_yellow}║ {light_blue} ██{light_yellow}║{light_blue}██{light_yellow}║╚{light_blue}██████{light_yellow}╔╝
╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝ ╚═════╝ V2.2
        {light_blue} Made with {reset_color}{light_yellow}<3{reset_color}{light_blue} by LR{light_yellow}#{reset_color}{light_blue}9856 {reset_color}                                

        {light_blue}Links {light_yellow}>{light_blue} {links}
        {light_blue}Param links {light_yellow}> {light_blue}{param_links}
        {light_blue}Errors {light_yellow}> {light_blue}{errors}
        {light_blue}Dorks amount {light_yellow}> {light_blue}{len(dorks)}
        {light_blue}Used dorks {light_yellow}> {light_blue}{len(used_dorks)}

"""
    print(banner)

def load():
    global links, param_links, errors
    links = 0
    param_links = 0
    errors = 0

def count_links():
    global links
    links += 1

def count_param_links():
    global param_links
    param_links += 1

def count_errors():
    global errors
    errors += 1

def start_threads():
    try:
        amount_threads = int(input(f"     Amount of threads {light_blue}> {light_yellow}"))
        for i in range(amount_threads):
            t = threading.Thread(target=get_dork)
            t.start()
            t.join()
    except ValueError:
        print(f"             {light_red}Error {light_yellow}>{light_red} Letters not allowed please use numbers ! {reset_color}")

def dorks_load():
    global dorks, used_dorks
    used_dorks = []
    dorksfile = open('searcher/dorks.txt', 'r', encoding='utf-8')
    dorks = dorksfile.readlines()

def get_dork():
    try:
        for dork in dorks:
            dork = dork.replace('\n', '')
            if dork in used_dorks:
                get_dork()
            else:
                used_dorks.append(dork)
                searcher(dork=dork)
    except:
        get_dork()

def searcher(dork):
    try:
        r = requests.get(f"https://www.google.com/search?q={dork}&num=200", cookies = {'CONSENT' : 'YES+'})
        soup = BeautifulSoup(r.text, 'html.parser')
        ass = soup.find_all('a')
        for a in ass:
            ctypes.windll.kernel32.SetConsoleTitleW(f"LR AIO V2.2 (Dork searcher) | LINKS : {str(links)} | PARAM LINKS : {str(param_links)}")
            a = str(a)
            if '<a href="/url?q=' in a:
                a = a.split('<a href="/url?q=')[1]
                a = a.split('">')[0].split('&amp')[0]
                a = unquote(a)
                if '.google.com' in a:
                    pass
                else:
                    count_links()
                    with open('searcher/links.txt', 'a', encoding='utf-8') as output_links:
                        output_links.write(a + '\n')
                    if '=' in a:
                        if "/search?q=" in a:
                            pass
                        else:
                            count_param_links()
                            banner_update()
                            ctypes.windll.kernel32.SetConsoleTitleW(f"LR AIO V2.2 (Dork searcher) | LINKS : {str(links)} | PARAM LINKS : {str(param_links)}")
                            with open('searcher/links_param.txt', 'a', encoding='utf-8') as output_links_param:
                                output_links_param.write(a + '\n')
                    else:
                        banner_update()
            else:
                pass
    except requests.exceptions.ConnectionError:
        count_errors()
        searcher(dork=dork)

colors_load()

os.system('cls')
print(f"""{light_blue}
██{light_yellow}╗{light_blue}     ██████{light_yellow}╗{light_blue}      █████{light_yellow}╗{light_blue} ██{light_yellow}╗{light_blue} ██████{light_yellow}╗{light_blue} 
██{light_yellow}║{light_blue}     ██{light_yellow}╔══{light_blue}██{light_yellow}╗ {light_blue}   ██{light_yellow}╔══{light_blue}██{light_yellow}╗{light_blue}██{light_yellow}║{light_blue}██{light_yellow}╔═══{light_blue}██{light_yellow}╗{light_blue}
██{light_yellow}║  {light_blue}   ██████{light_yellow}╔╝{light_blue}    ███████{light_yellow}║{light_blue}██{light_yellow}║{light_blue}██{light_yellow}║  {light_blue} ██{light_yellow}║{light_blue}
██{light_yellow}║  {light_blue}   ██{light_yellow}╔══{light_blue}██{light_yellow}╗    {light_blue}██{light_yellow}╔══{light_blue}██{light_yellow}║{light_blue}██{light_yellow}║{light_blue}██{light_yellow}║   {light_blue}██{light_yellow}║{light_blue}
███████{light_yellow}╗{light_blue}██{light_yellow}║{light_blue}  ██{light_yellow}║ {light_blue}   ██{light_yellow}║ {light_blue} ██{light_yellow}║{light_blue}██{light_yellow}║╚{light_blue}██████{light_yellow}╔╝
╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝ ╚═════╝ V2.2
        {light_blue} Made with {reset_color}{light_yellow}<3{reset_color}{light_blue} by LR{light_yellow}#{reset_color}{light_blue}9856 {reset_color}                                
""")

dorks_load()
load()
start_threads()