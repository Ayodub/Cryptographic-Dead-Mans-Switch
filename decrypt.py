from cryptography.fernet import Fernet
import glob
import os

currentdirectory = os.getcwd()   # Get current directory (don't want to encrypt system files)

def load_key():   
    return open("key.key", "rb").read()

def encrypt(filename, key): 
    f = Fernet(key)


key = load_key()  

f = Fernet(key)   

print('\n Beginning recursive decryption...\n\n')

for x in glob.glob(currentdirectory +'/**/*/*', recursive=True):    

    filepath = os.path.join(currentdirectory, x)
    newfile = os.path.join(currentdirectory, os.path.splitext(x)[0])
   
    if os.path.isfile(filepath):   #make sure it is a file, otherwise if it is folder it will give error
        print('>>> Located: \t' + filepath + '')
        print('>>> Decrypted: \t' + newfile + '\n')
        with open(filepath, "rb") as file:            
            file_data = file.read()
       
        decrypted_data = f.decrypt(file_data)  

        with open(newfile, "wb") as file:  
            file.write(decrypted_data)

        os.remove(filepath)  
