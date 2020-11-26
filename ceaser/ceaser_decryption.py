# imports
import sys

# ======================================= ceaser_decryption ======================================= #
#function: ceaser_decryption
#   parameters: 2, str_encrypted_text(string), int_shift(integer)
#   return: 1, plain_text(string)
#   functionality: decrypts the input encryption text with the shift algorithm and 
#       returns the original plain text
def ceaser_decryption(str_encrypted_text,int_shift):
    try:
        # initialize return
        str_plain_text = None
        # check if the shift value is a valid integer
        # and if the plain text isn't empty or filled with whitespace
        if isinstance(int_shift,int) and str_encrypted_text.strip():
            str_plain_text = ""

            ## loop over each character in the encryption text
            for c in str_encrypted_text:    
                # check if character is an upper case letter
                if (ord(c) >= 65) and (ord(c) <= 90):
                    str_plain_text += chr((ord(c) - 65 - int_shift) % 26 + 65)
                # check if character is a lower case letter
                elif (ord(c) >= 97) and (ord(c) <= 122):
                    str_plain_text += chr((ord(c) - 97 - int_shift) % 26 + 97)
                # pass the non letter characters
                else:
                    str_plain_text += c
                    
        return str_plain_text    
    except:
        print("Unexpected error:", sys.exc_info()[0])

