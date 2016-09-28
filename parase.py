import urllib.request
import re

url = 'http://www.pythonprogramming.net'
values = {'s':'basics', 'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url,data)
resp = urllib.request.urlopne(req)

respData =resp.read()

# print (respData)

paragraphs = re.findall(r'<p>(.*?)</p',str(respData)

for eachP in paragraphs:
    print (eachP)
