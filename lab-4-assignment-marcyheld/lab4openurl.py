from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.data.pr4e.org/romeo.txt'
html = urlopen(url, context=ctx).read().decode()

print (html[:100]) # print chars at index 0 - 99

charCount = 0
for char in html:
    charCount += 1

print (charCount)
