"""

Author: Omkar Dixit
Source: IDEA Developers

"""

# Find IP Address Geo Location  

from urllib.request import urlopen
from bs4 import BeautifulSoup

class IPLocationFinder:
    def __init__(self):
        self.keycdn = "https://tools.keycdn.com/geo?host="

    def findIpLocation(self, ipAddr):
        self.keycdn = self.keycdn + ipAddr
        html_page = urlopen(self.keycdn)
        soup = BeautifulSoup(html_page, 'html.parser')

        jsonData = soup.find("table").text.strip()
        jsonData = jsonData.splitlines()

        dataLength = len(jsonData) - 1
        for x in range(0, dataLength, 2):
            if jsonData[x] and jsonData[x+1]:
                data = jsonData[x] + "=" + jsonData[x+1]
                print(data)
        
    def startApp(self, ipAddr):
        if not ipAddr:
            print("Please Enter a Valid Ip Address!")
        else:
            self.findIpLocation(ipAddr)

if __name__== "__main__":
    ipLoc = IPLocationFinder()
    # ipLoc.startApp("172.217.10.14")
    ipLoc.startApp("2605:6001:e15b:9500:f0b2:fa0f:7536:82f")