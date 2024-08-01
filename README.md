# XMLRPC-Auditor
Auditing tools for WordPress's xmlrpc.php. Frequently, while testing WordPress, we come across the xmlrpc.php file, and we know that it should be disabled or restricted from being accessed by the public. The xmlrpc.php file can allow an attacker to perform SSRF (blind), CSPS, and brute-force attacks if the respective options are active. Manually testing for these vulnerabilities is very time-consuming, and in my testing experience, I often felt the need for some automation or a tool to perform these checks automatically, so here it is.

XMLRPC-Auditor is at its initial stage; I developed it to automatically test for SSRF and brute-force attacks. I will add more features to it in the future. If you have a better idea or something new to contribute, feel free to issue a pull request or fork this repository.


### Usage
This tool has only one option which is `-url`. It will ask for a WordPress installation url and scan for it.

** Testing for SSRF attack**
+ It will first detect the options for SSRF
+ Then it will ask whether you want to test SSRF or not. If yes then it will ask for listner host
+ Make sure you have your burp collaborator client or any listner ready.
![git1](https://github.com/user-attachments/assets/72761e85-a335-4c38-ba7c-c921a85f8ec4)

** Testing for brute forece attack**
+ It will again detect options which will let us do brute force
+ It will ask for concent and then for username and password wordlist path
+ After that it will start the attack and print the valid credentials.
  ![git2](https://github.com/user-attachments/assets/f93edeae-144e-4860-808f-84b85b7c2f17)


