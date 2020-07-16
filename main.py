import time
import signal
import threading #I need to have input and countdown operating at same time
#import datetime    Date time module could be used if the script was running over longer periods such as days/weeks/months
from cryptography.fernet import Fernet
import glob
import os
from os import remove
from sys import argv  #for self delete


#-----------------------------#
#Note on structure of combined file: First the key generation is placed at the top so that the person can start the count
#at a long period such as 1 month, and immediately hide the key. Next the DMS runs, and finally the actual encryption.
#All of the definitions for encryption are placed at the top, and only the recursive selection and encryption itself are
#placed last.

clock=0            #define variables early so that I set up an error handling loop
self_destruct=0


currentdirectory = os.getcwd()   # Get current directory (don't want to encrypt system files)

def write_key():  #generate encryption key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():   #loads the encryption key
    return open("key.key", "rb").read()

def encrypt(filename, key):  
    f = Fernet(key)

write_key() # load the previously generated key

key = load_key()  # initialize the Fernet class

f = Fernet(key)   #file_list = os.listdir(currentdirectory)

starttime=time.time() 
lasttime=starttime 

warning= input("Your  decryption key has been generated. It is recommended that you keep this in a separate location to the \nfiles which you wish to encrypt. Press enter to continue..")

while True:    #infinite loop used to control errors from input
    try:
        while self_destruct != "y" and self_destruct != "n":
            self_destruct= input("Do you want this program to self-delete at end of execution? y/n :")
        break
    except ValueError:
        print("please type 'y' or 'n'")

clock = input("\n How many seconds until switch is triggered? : ")

trigger = int(clock)

def interrupted(signum, frame):          #This is the 'alarm clock', which activates if it reaches timer
    pass

signal.signal(signal.SIGALRM, interrupted) #it will print 'files encrypted' instead of simply 'alarm clock'

def count(): 
    global s    
    while s >= 0:
        print(s)
        s -= 1
        time.sleep(1)

def user_reset():  # this is the alert for interaction and the reset trigger when interacted with.
    global s
    print(f'Encryption will begin in {trigger} seconds')
    interact = input()
    print('input received, reseting.')
    s = trigger
    user_reset()


s = trigger
x= threading.Thread(target=user_reset)   #for some reason the .start/.join method on the end of the threading didnt work, it needed to be assigned to a variable
x.start()
y= threading.Thread(target=count)
y.start()

#-------------This is where the encryption script starts------------ Need to fix threading---

y.join()

print("Beginning recursive encryption..")

for x in glob.glob(currentdirectory +'/**/*/*', recursive=True):    # Main loop to encrypt all files recursively
# double asterix ** tells program to encrypt all types of files

    fullpath = os.path.join(currentdirectory, x)
    fullnewf = os.path.join(currentdirectory, x + '.aes')
    # Encrypt
    if os.path.isfile(fullpath):   #make sure it is a file, otherwise if it is folder it will give error
        print('>>> Located: \t' + fullpath + '')
        print('>>> Encrypted: \t' + fullnewf + '\n')
        with open(fullpath, "rb") as file:      #rb= "read in binary"
            file_data = file.read()
       
        encrypted_data = f.encrypt(file_data)  # encrypt data

        with open(fullnewf, "wb") as file:  # wb = "write in binary"
            file.write(encrypted_data)
        
        os.remove(fullpath)  #removes the old file


print('\n Encryption complete...\n\n')

if self_destruct == "y":          #-------------------------------------------------
    remove(argv[0])              #comment these to make self-destruct not possible 
elif self_destruct == "n":      #-------------------------------------------------
    quit()


