import urllib2, re
ip = raw_input("Enter The Victim Ip Address: ")
print """
 _   __                   ___                  
| | / /                  / _ \                 
| |/ /  __ _ _ __ __ _  / /_\ \_   _  __ _ ____
|    \ / _` | '__/ _` | |  _  | | | |/ _` |_  /
| |\  \ (_| | | | (_| | | | | | |_| | (_| |/ / 
\_| \_/\__,_|_|  \__,_| \_| |_/\__, |\__,_/___|
                                __/ |          
                               |___/
"""
response  = urllib2.urlopen("http://www.whatismyipaddress.com/ip/"+ip)
payload = response.read()
result_lok = re.findall("Country:</th><td>(.*?) <img", payload)
result_host = re.findall("Hostname:</th><td>(.*?)</td></tr>", payload)
result_isp = re.findall("ISP:</th><td>(.*?)</td></tr>", payload)
result_org = re.findall("Organization:</th><td>(.*?)</td></tr>", payload)
result_ass = re.findall("Assignment:</th><td><a href='/dynamic-static'>(.*?)</a></td></tr>", payload)

for lokasyon in result_lok:
    print "Lokasyon: "+lokasyon
for host in result_host:
    print "Host: "+host
for isp in result_isp:
    print "ISP: "+isp
for org in result_org:
    print "Organizasyon: "+org
for ass in result_ass:
    print "Tur: "+ass

raw_input("Press any key to exit.. ")
