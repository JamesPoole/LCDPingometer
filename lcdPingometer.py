#!/usr/bin/python

####################
#Author: James Poole
#Date: 18/01/2016
#lcdPingometer.py
####################

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD() #make an object called lcd

#the script to be executed
#this will ping google.com (8.8.8.8) take the response time from the output
cmd = "sudo ping -c 1 8.8.8.8 | grep time= | awk '{print $7}'"

#start up the lcd screen
lcd.begin(16, 1)

#the function that will take the cmd string and execute it as a command
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output


while 1:
    pingCmd = run_cmd(cmd) #execute cmd and assign output to pingcmd
    strLength = len(pingCmd) #get the amount of characters in pingcmd
    print strLength
    print pingCmd
    
    
    if strLength < 1: #if pingcmd contains no characters => there is no connection
        lcd.clear()
        lcd.message('Pingometer\n')
        lcd.message('No Connection')
    else: #otherwise there is a connection and it will print the ping
        lcd.clear()
        lcd.message('Pingometer\n')
        lcd.message('Ping %s' % (pingCmd))
    sleep(2)
