#WP Super Cache WordPress Plugin <= 1.7.1 - Authenticated RCE 

#Simple WP Super Cache WordPress Plugin Authenticated RCE Checker - Himash

#importing modules
import requests
import time
import sys
import argparse

#Banner Display
print("""


/////////////////////////////////////////
////////////         ///////////////////
//////////////   //////////////////////
/////////////// //////////////////////
/////////////////////////////////////
@Himash
 
Simple WP Super Cache WordPress Plugin Authenticated RCE Scanner

Example : python3 WP_Super_Cache_RCE.py -s https://target.com

""")

def main(arguments):
    
    if arguments.s:
        scan(arguments.s)


def scan(arg):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Connection": "keep-alive",
               "Content-Type": "application/x-www-form-urlencoded",
               "Connection": "keep-alive"
               }

        url = arg + "/wp-content/plugins/wp-super-cache/"
        print ("\nScanning the Target.......! \n")
        scan_response = requests.get(url)

        if scan_response.status_code == 200:
            print(arg + " Possibly VULNERABLE ...!")

        else:
            print(arg +  " is not VULNERABLE\n")

    except:
        print(" Unable to Scan the Target ")



if __name__ == "__main__":
    try:
        description = 'Simple WP Super Cache WordPress Plugin Authenticated RCE Scan'
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument("-s",type=str, help= " To Scan the Target Type -s ")
        arguments = parser.parse_args()
        main(arguments)

    except(KeyboardInterrupt) as e:
        sys.exit(0)


