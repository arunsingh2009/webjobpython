import requests
import time
print ("hello world")
url = 'https://www.google.co.in/'
r = requests.get(url)
print ("status code  :",r.status_code)