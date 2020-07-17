#Testing Procedures


##Test 1: Encrypting File Types

The Cryptographic Dead Man's Switch application was tested for it's ability to encrypt multiple file types, while moving through directories. This was completed by creating multiple directories containing text files and images, although videos were not possible. There were several expectations during this task: First, the program would encrypt all files found to .aes, regardless of it they are text or images/ Second, the program will not encrypt folders, but instead move into them. Third, the program will successfully repeat this series of tasks until it reaches the end of the path at which point it will terminate. These expectations were all successfully met.



##Test 2: Restoring File's Original Content Through Decryption

It was considered that, even if encryption was successful, that files may fail to decrypt back to their original state. To test this both images as well as text files were again uploaded, and this time each were given content. Upon encryption this content was scrambled and unreadable. However, upon decryption it was all accurately restored to it's original state without any damage or errors.
