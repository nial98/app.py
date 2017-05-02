import RPi.GPIO as GPIO
import time
import urllib3
import certifi
import json

GPIO.setmode(GPIO.BCM)
PIR_PIN=7
GPIO.setup(PIR_PIN, GPIO.IN)
sec = 10
try:   
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(2)
    print "ready"
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    while True:
            if GPIO.input(PIR_PIN):
                    sec = 0
                    
            else:
                    sec += 1
                    
            time.sleep(1)
            if sec >= 10:
                    print "not occupied"
                    print "time since motion detected", sec, "seconds"
                    r = http.request('GET' , '52.60.213.136/unoccupied')
                    if not r.status == 200:
                           print 'Server unreachable: ' + str(r.status)
            else:
                    print "occupied"
                    r = http.request('GET', '52.60.213.136/occupied')
                    if not r.status == 200:
                           print 'Server unreachable: ' + str(r.status)
                           
except KeyboardInterrupt:
        print "quit"
        GPIO.cleanup()