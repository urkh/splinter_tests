from splinter import Browser

#user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36"
user_agent = "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Arora/0.11.0 Safari/533.3"

ip = '101.79.242.17' # Korea https proxy 
port = '8080'
 
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

browser.visit('https://www.whatismyip.com/')
