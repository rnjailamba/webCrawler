import urllib2, httplib
from bs4 import BeautifulSoup
import requests
import sys

def append_log(message):
    print message

def get_web_page(address):
    try:
        user_agent = 'Mozilla/5.0'
        headers = { 'User-Agent' : user_agent }
        request = urllib2.Request(address, None, headers)
        response = urllib2.urlopen(request, timeout=20)
        try:
            return response.read()
        finally:
            response.close()
    except urllib2.HTTPError as e:
        error_desc = httplib.responses.get(e.code, '')
        append_log('HTTP Error: ' + str(e.code) + ': ' +
                  error_desc + ': ' + address)
    except urllib2.URLError as e:
        append_log('URL Error: ' + e.reason[1] + address)
    except Exception as e:
        append_log('Other Error: ' + str(e) + address)

def process_web_page(data):
    if data is not None:
        soup = BeautifulSoup(data ,"lxml")
        print(soup)
    else:
        get_data()
        print('do something')
        pass
         # do something else

def request_data():
    url = raw_input("Enter a website to extract the URL's from/type exit to exit: ")
    if url == 'exit':
        sys.exit()   
    data = get_web_page(url)    
    process_web_page(data)  

def get_data():
    url = raw_input("Enter maximum number of Links to be parsed")
    request_data()


get_data()

# data = get_web_page('www.doesnotexistblah.com/')
# process_web_page(data)

# data = get_web_page('https://github.com/fdxxxxx')
# process_web_page(data)

#data = get_web_page('http://docs.python.org/copyright.html')
#process_web_page(data)
