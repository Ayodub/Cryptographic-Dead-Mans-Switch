import time                   
import signal          
import threading    #I need to have input and countdown operating at same time
# import datetime    Date time module could be used if the script was running over longer periods such as days/weeks/months
starttime=time.time() 
lasttime=starttime 


trigger = input("How many seconds until switch is triggered? : ")
TIMEOUT = int(trigger)

def interrupted(signum, frame):          #This is the 'alarm clock', which activates if it reaches timer
    pass

signal.signal(signal.SIGALRM, interrupted) #this calls the process on line 26 so that it will print 'files encrypted' instead of simply 'alarm clock'


def count():      #This is the count, with the countdown printed to screen.
    global s
    while s < TIMEOUT:
            print(format(s))
            s = s+1
            time.sleep(1)    
    print("Files have been encrypted")


def i_input():    #this is the alert for interaction and the reset trigger when interacted with.
    global s
    print(f'Encryption will begin in {TIMEOUT} seconds')
    interact = input()
    print('input received, reseting.')
    s=0
    i_input
        
signal.alarm(TIMEOUT)


s = 0
threading.Thread(target=i_input).start()
threading.Thread(target=count).start()
