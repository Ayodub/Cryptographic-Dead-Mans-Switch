import time
import signal
import threading #I need to have input and countdown operating at same time
#import datetime    Date time module could be used if the script was running over longer periods such as days/weeks/months

starttime=time.time() 
lasttime=starttime 

clock = input("How many seconds until switch is triggered? : ")
trigger = int(clock)

def interrupted(signum, frame):          #This is the 'alarm clock', which activates if it reaches timer
    pass

signal.signal(signal.SIGALRM, interrupted) #it will print 'files encrypted' instead of simply 'alarm clock'

def count(): 
    global s    
    while s > 0:
        print(s)
        s -= 1
        time.sleep(1)
    print("Files have been encrypted")

def user_reset():  # this is the alert for interaction and the reset trigger when interacted with.
    global s
    print(f'Encryption will begin in {trigger} seconds')
    interact = input()
    print('input received, reseting.')
    s = trigger
    user_reset()


s = trigger
threading.Thread(target=user_reset).start()
threading.Thread(target=count).start()
