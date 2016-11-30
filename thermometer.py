import os
import sys
import glob
import time

import urllib
import urllib2
 
from collections import deque

q = deque()

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
url = 'http://climatestation-mdiastech.rhcloud.com/monitor/add/'
device_key='YOUR-KEY'
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        q.append(temp_c)
        if len(q) > 20:
            q.popleft()
        return temp_c, (float(sum(q))/len(q))
	
def post():
    try:
        temp, avg = read_temp()
        values = { 'key':device_key,
                   'temperature':temp,
                   'average':avg }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        if response.read() != 'OK':
            print 'Error uploading data'
            print response.read()
    except urllib2.HTTPError as e:
        print e
    except urllib2.URLError as e:
        print e
        time.sleep(60)
    finally:
        sys.stdout.flush()

print "Starting thermometer reader"
sys.stdout.flush()
while True:
    post()
    time.sleep(60)
