import urllib.request
import json
class myMessage:
    api_token = '3742a5e7520a2c0513050b882d1643e8c1cc76f452d65e2c20c6c373348f21c4'
    to = 'nessie'
    message = 'hello world'

def main():
    URL = 'https://whoomp.cs.uwaterloo.ca/458a3/api/plain/inbox'
    message = myMessage()
    jmessage = json.dump(message)
    req = urllib.request.Request(URL,data=jmessage,method="POST")
    urllib.request.urlopen(req)
