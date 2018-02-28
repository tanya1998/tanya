#!/usr/bin/env python

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading=True

def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading=False
    GPIO.cleanup()

#signal.signal(signal.SIGINT,end_read)

MIFAREReader=MFRC522.MFRC522()

print "Welcome"

j=0
while continue_reading:
    (status,TagType)=MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    (status,uid)=MIFAREReader.MFRC522_Anticoll()
    if (status==MIFAREReader.MI_OK) and (j%2 == 0):
        print "card detected"
        print "Card Read UID: "+ str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    elif j%2 == 0:
        print "card not detected"
    j = j+1
        
