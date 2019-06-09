#import sys
from pulsesensor import Pulsesensor
import time
#import urllib
import urllib2
#import json
#import requests
#import csv
# Getting the pulse values from sensor
p = Pulsesensor()
p.startAsyncBPM()

try:
    file = open('heartbeat.csv','a')
    
    while True:
        bpm = p.BPM
        if bpm > 0:
            print("BPM: %d" % bpm)
        else:
            print("No Heartbeat found")
        time.sleep(10)
        # Writing these values to ThingSpeak ChannelNo:795828
        APIKEY = 'TGLJTVAC7MJ7O0HT'
        api_url = 'https://api.thingspeak.com/update?api_key=%s&field1=0' % APIKEY
        conn = urllib2.urlopen(api_url + 'field1 = %s' % bpm)
        print (conn.read())
        conn.close
        file.write(bpm)
        file.write("\n")
    file.close()
    test = 0
    timeout = 60   # [seconds]

    timeout_start = time.time()

    while time.time() < timeout_start + timeout:
        if test == 1:
            break
        test -= 1
    

except:
    p.stopAsyncBPM()

# Creating file to save the values
# getting values using API from ThingSpeak