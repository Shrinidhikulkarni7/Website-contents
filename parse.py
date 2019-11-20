import requests

f= open("dicc.txt" ,"r")
while(1):
    str= f.readline()
    str=str.strip()
    print str

    response= requests.get('https://www.adithyabhat.com/#/' +str)
    if (response.status_code ==200):
        print "Success"
