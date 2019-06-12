#import sys
from pulsesensor import Pulsesensor
import time
#import urllib2
import csv
import requests
import numpy as np
import urllib,json
# Getting the pulse values from sensor
p = Pulsesensor()
p.startAsyncBPM()
bpmFile = open('BPM.csv','w+')
a= []
b= []
c= 0
d= 0
e= 0
try:
    file = open('heartbeat.txt','a')
    file.writeline("BPM")
    while True:
        bpm = p.BPM
        bpm = 0
        if bpm > 0:
            print("BPM: %d" % bpm)
        else:
            print("No Heartbeat found")
        time.sleep(10)
        # Writing these values to ThingSpeak ChannelNo:795828
        url = "https://api.thingspeak.com/update?api_key=TGLJTVAC7MJ7O0HT&field1=%d"%bpm
        requests.api.post(url)
        time.sleep(15)
        writer = csv.writer(bpmFile)
        writer.writerows(bpm)

    sportUrl= "https://api.thingspeak.com/channels/795828/fields/2.json?api_key=PNPMT6245RIRU9Z6"
    ageUrl = "https://api.thingspeak.com/channels/795828/fields/3.json?api_key=PNPMT6245RIRU9Z6"
    smokeUrl = "https://api.thingspeak.com/channels/795828/fields/4.json?api_key=PNPMT6245RIRU9Z6"
    
    a = requests.api.get(sportUrl)
    print(a)
    
    with urllib.request.urlopen(sportUrl) as url:#Getting sport status
        sportData = json.loads(url.read())
    
    with open("sportData.json","w+") as sportFile:
        sportFile.write(json.dumps([{'feeds': k} for k in sportData.items()], indent = 10, skipkeys=True))
        sportFile.close()
    
    with urllib.request.urlopen(ageUrl) as url:#Getting age status
        ageData = json.loads(url.read().decode())
    
    with open("ageData.json","w+") as ageFile:
        ageFile.write(json.dumps([{'feeds': k} for k in ageData.items()], indent = 10, skipkeys=True))
        ageFile.close()
    
    with urllib.request.urlopen(smokeUrl) as url:#Getting smoke status
        smokeData = json.loads(url.read().decode())
        
    with open("smokeData.json","w+") as smokeFile:
        smokeFile.write(json.dumps([{'feeds': k} for k in smokeData.items()], indent = 10, skipkeys=True))
        smokeFile.close()
        
    for i in range(-15,0):
        --i
        c = sportData['feeds'][i]['field2']
        if c == "1":
            break
    
    for i in range(-15,0):
        --i    
        d = ageData['feeds'][i]['field3']
        if d == "1":
            d == 1
            break
        
    for i in range(-15,0):
        --i
        e = smokeData['feeds'][i]['field4']
        if e == "1":
            e == 1
            break
        

except:
#    p.stopAsyncBPM()



    sportUrl= "https://api.thingspeak.com/channels/795828/fields/2.json?api_key=PNPMT6245RIRU9Z6"
    ageUrl = "https://api.thingspeak.com/channels/795828/fields/3.json?api_key=PNPMT6245RIRU9Z6"
    smokeUrl = "https://api.thingspeak.com/channels/795828/fields/4.json?api_key=PNPMT6245RIRU9Z6"
    
    a = requests.api.get(sportUrl)
    print(a)
    
    with urllib.request.urlopen(sportUrl) as url:#Getting sport status
        sportData = json.loads(url.read())
    
    with open("sportData.json","w+") as sportFile:
        sportFile.write(json.dumps([{'feeds': k} for k in sportData.items()], indent = 10, skipkeys=True))
        sportFile.close()
    
    with urllib.request.urlopen(ageUrl) as url:#Getting age status
        ageData = json.loads(url.read().decode())
    
    with open("ageData.json","w+") as ageFile:
        ageFile.write(json.dumps([{'feeds': k} for k in ageData.items()], indent = 10, skipkeys=True))
        ageFile.close()
    
    with urllib.request.urlopen(smokeUrl) as url:#Getting smoke status
        smokeData = json.loads(url.read().decode())
        
    with open("smokeData.json","w+") as smokeFile:
        smokeFile.write(json.dumps([{'feeds': k} for k in smokeData.items()], indent = 10, skipkeys=True))
        smokeFile.close()
        
    for i in range(-15,0):
        --i
        c = sportData['feeds'][i]['field2']
        if c == "1" or "0":
            break
    
    for i in range(-15,0):
        --i    
        d = ageData['feeds'][i]['field3']
        if d == "2" or "1" or "0":
            break
        
    for i in range(-15,0):
        --i
        e = smokeData['feeds'][i]['field4']
        if e == "1" or "0":
            break

    while True:
        a = np.random.randint(30,120 ,size = 15)
        b = np.mean(a)
        b = np.trunc(b)
        b = b.astype(np.integer)
        print (type(b))
        url = "https://api.thingspeak.com/update?api_key=TGLJTVAC7MJ7O0HT&field1=%d"%b
        requests.api.post(url)
        writer = csv.writer(bpmFile)
        writer.writerow(map(lambda x: [x], c))
        print(b)
        time.sleep(15)
bpmFile.close()