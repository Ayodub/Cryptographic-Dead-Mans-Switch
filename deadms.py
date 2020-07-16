import time
import threading 
#import datetime    Date time module could be used if the script was running over longer periods such as days/weeks/months


starttime=time.time() 
lasttime=starttime 

clock = input("How many seconds until switch is triggered? : ")
trigger = int(clock)

def count(): 
    global s    
    while s > 0:
        print(s)
        s -= 1
        time.sleep(1)
    print("Files have been encrypted")


def user_reset(): 
    global s
    print(f'Encryption will begin in {trigger} seconds')
    interact = input()
    print('input received, reseting.')
    s = trigger
    user_reset()


s = trigger
threading.Thread(target=user_reset).start()
threading.Thread(target=count).start()
