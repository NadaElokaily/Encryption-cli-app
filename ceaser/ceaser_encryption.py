# imports
import sys

# ======================================= ceaser_encryption ======================================= #
#function: ceaser_encryption
#   parameters: 2, str_plain_text(string), int_shift(integer)
#   return: 1, encrypted_text(string)
#   functionality: encrypts the input plain text with the shift algorithm
def ceaser_encryption(str_plain_text,int_shift):
    try:
        # initialize return
        str_encrypted_text = None
        # check if the shift value is a valid integer
        # and if the plain text isn't empty or filled with whitespace
        if isinstance(int_shift,int) and isinstance(str_plain_text,str):
            if str_plain_text.strip():
                str_encrypted_text = ""

                ## loop over each character in the plain text
                for c in str_plain_text:    
                    # check if character is an upper case letter
                    if (ord(c) >= 65) and (ord(c) <= 90):
                        str_encrypted_text += chr((ord(c) - 65 + int_shift) % 26 + 65)
                    # check if character is a lower case letter
                    elif (ord(c) >= 97) and (ord(c) <= 122):
                        str_encrypted_text += chr((ord(c) - 97 + int_shift) % 26 + 97)
                    # pass the non letter characters
                    else:
                        str_encrypted_text += c
                        
        return str_encrypted_text
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
