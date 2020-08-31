import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 lovehacker.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;96m|', '\x1b[1;92m/', '\x1b[1;95m-', '\x1b[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Keluar'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0003)


logo = '\033[1;95m╭━━━╮\033[1;95m┃╭━╮┃\033[1;95m┃┃╱┃┣━━┳┳━━┳━━┳━╮\033[1;95m┃┃╱┃┃╭╮┣┫━━┫┃━┫╭╯\033[1;95m┃╰━╯┃╭╮┃┣━━┃┃━┫┃\033[1;95m╰━━╮┣╯╰┻┻━━┻━━┻╯\033[1;95m╱╱╱╰╯\033[1;94m-----------------------------------------------\033[1;92mCoder   :\033[1;96mTech Qaiser\033[1;92mGithub  :\033[1;96mhttps://github.com/TechQaiser\033[1;92mFacebook:\033[1;96mQaiser Abbas\033[1;92mYoutube :\033[1;96mTech Qaiser\033[1;92mNote :\033[1;96mThis Is only For Educational Purpose\033[1;92mNew Update :\033[1;96m Identity Problem Fixed 100% If You Login With Acces Token\033[1;94m-----------------------------------------------'
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
os.system('clear')
print '｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡'
os.system('clear')
jalan('\x1b[1;93m------------------------------------')
jalan('\x1b[1;96m /$$$$$$$  /$$                     /$$      ')
jalan('\x1b[1;96m| $$__  $$| $$                    | $$      ')
jalan('\x1b[1;96m| $$  \\ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$')
jalan('\x1b[1;96m| $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/')
jalan('\x1b[1;96m| $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/ ')
jalan('\x1b[1;96m| $$  \\ $$| $$ /$$__  $$| $$      | $$_  $$ ')
jalan('\x1b[1;96m| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \\  $$')
jalan('\x1b[1;96m|_______/ |__/ \\_______/ \\_______/|__/  \\__/')
jalan('\x1b[1;96m$$\\      $$\\            $$$$$$\\  $$\\          ')
jalan('\x1b[1;96m$$$\\    $$$ |          $$  __$$\\ \\__|          ')
jalan('\x1b[1;96m$$$$\\  $$$$ | $$$$$$\\  $$ /  \\__|$$\\  $$$$$$\\  ')
jalan('\x1b[1;96m$$\\$$\\$$ $$ | \\____$$\\ $$$$\\     $$ | \\____$$\\ ')
jalan('\x1b[1;96m$$ \\$$$  $$ | $$$$$$$ |$$  _|    $$ | $$$$$$$ |')
jalan('\x1b[1;96m$$ |\\$  /$$ |$$  __$$ |$$ |      $$ |$$  __$$ |')
jalan('\x1b[1;96m$$ | \\_/ $$ |\\$$$$$$$ |$$ |      $$ |\\$$$$$$$ |')
jalan('\x1b[1;96m\\__|     \\__| \\_______|\\__|      \\__| \\_______| ')
jalan('\x1b[1;93m              Welcome to BlackMafia')

def masuk():
    os.system('clear')
    print logo
    print 36 * '\x1b[1;91m\xe2\x96\x93'
    print '\x1b[1;97m{\x1b[1;92m01\x1b[1;97m} Login Token Facebook'
    print '\x1b[1;97m{\x1b[1;92m02\x1b[1;97m} Download Token App'
    print '\x1b[1;97m{\x1b[1;92m03\x1b[1;97m} Download Token App'
    print '\x1b[1;97m{\x1b[1;92m04\x1b[1;97m} Login With Facebook'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Exit'
    print 36 * '\x1b[1;91m\xe2\x96\x93'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;90mSlect Options\x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Fill Correctly !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        ambil_token()
    elif msuk == '3' or msuk == '03':
        ambil_link()
    elif msuk == '4' or msuk == '04':
        login()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Fill Correctly !'
        pilih_masuk()


def tokenz()
