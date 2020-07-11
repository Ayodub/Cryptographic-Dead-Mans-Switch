import time                   
import signal          
import threading    #I need to have multiple processes running at once, rather than a single flowing script
# import datetime    Date time module could be used if the script was running over longer periods such as days/weeks/months

trigger = input("How many seconds until switch is triggered?")
TIMEOUT = int(trigger)

def interrupted(signum, frame):
    print('exit')
    signal.signal(signal.SIGALRM, interrupted)


def i_input():    #this is the alert for interaction and the reset trigger when interacted with.
    try:
        print(f'Encryption will begin in {TIMEOUT} seconds')
        foo = input()
        print('input received, reseting.')
        i_input()
    except:
        return
    signal.alarm(TIMEOUT)


def count(s):      #This is the count, with the countdown printed to screen.
    s==TIMEOUT
    while s<= TIMEOUT:
        print('count : {}'.format(s))
        s = s+1
        time.sleep(1)
    print("files have been encrypted")


threading.Thread(target = i_input).start()
countThread = threading.Thread(target=count, args=(0,));
countThread.start();
