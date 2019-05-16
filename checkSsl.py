import socket
import ssl


import sys
#https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python
#get issuer and subject usage python checkSsl.py 1 www.google.com
if len(sys.argv)>2 and int(sys.argv[1])==1: 
    hostname = sys.argv[2]
    ctx = ssl.create_default_context()
    s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
    s.connect((hostname, 443))
    cert = s.getpeercert()
    print cert.get('subject')
    print cert.get('issuer')
#check links are correct to add ssl.txt get details from option 1 and add this format link;subject;issuer; with semicolons
if len(sys.argv)>1 and int(sys.argv[1])==2:
    with open('ssl.txt','r') as f:
        data=f.read()
    
    data_ssl=data.replace('\n','').split(';')

    for i in range(0,len(data_ssl)-1,3):
        ctx1 = ssl.create_default_context()
        hostname=data_ssl[i]
        s1 = ctx1.wrap_socket(socket.socket(), server_hostname=hostname)
        s1.connect((hostname, 443))
        cert = s1.getpeercert()
        if str(cert.get('subject'))!=data_ssl[i+1] or str(cert.get('issuer'))!=data_ssl[i+2]:
            print("Attention")
