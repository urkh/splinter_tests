from splinter import Browser
import os
BASE_PATH = os.getcwd()

user_agent = "Mozilla/5.0 (X11; U; Windows x86_128; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Arora/0.11.0 Safari/533.3"

ip = '112.133.213.181' # Indian https proxy 
port = 80
 
proxy = {
    'network.proxy.type': 1,
    'network.proxy.http': ip,
    'network.proxy.http_port': port,
    'network.proxy.ssl': ip,
    'network.proxy.ssl_port': port,
    'network.proxy.socks': ip,
    'network.proxy.socks_port': port,
    'network.proxy.ftp': ip,
    'network.proxy.ftp_port': port           
}
 
browser = Browser('firefox', user_agent=user_agent, profile_preferences=proxy)
browser.visit('https://duckduckgo.com/?q=ip')
browser.screenshot(name=BASE_PATH, suffix='_ip.png')

browser.visit('https://duckduckgo.com/?q=user+agent')
browser.screenshot(name=BASE_PATH, suffix='_useragent.png')
