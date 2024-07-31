#!/bin/env python3
import argparse
from engine import *




def main():
    banner = """
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*" 
.....   -~~:<` !    ~?T#$$@@W@*?$$      /` 
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :   
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`    
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``       You're hacking WordPress? Again?  
?MXT@Wx.~    :     ~"##*$$$$M~ 
"""
    parser = argparse.ArgumentParser(description="Wordpress XMLRPC Auditing Script")
    parser.add_argument("-url", "-u", required=True, type=str, help="Full url of WordPress installation. ex: https://example.com/")
    args = parser.parse_args()

    url = args.url
    print(banner)
    hackme = xmlrpc(url)
    hackme.scan()   
    
if __name__=="__main__":
    main()