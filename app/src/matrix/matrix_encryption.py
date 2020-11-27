# imports
import sys
from matrix_macros import ENCRYPT_KEY_MATRIX
from matrix_encryption_helpers import plain_text_to_plain_matrix, matrix_multiplication


# ======================================= matrix_encryption ======================================= #
#function: matrix_encryption
#   parameters: 1, str_plain_text(string)
#   return: 1, int_encrypted_matrix(array of integers)
#   functionality: encrypts plain text and returns the encrypted resultant matrix
def matrix_encryption(str_plain_text):
    try:
        # initialize the return
        int_encrypted_matrix = None
        # check if input text is not empty or consisting of white space only and is a sring
        if isinstance(str_plain_text, str):
            if str_plain_text.strip():
                # get the plain text matrix
                int_plain_matrix = plain_text_to_plain_matrix(str_plain_text)

                # check if the plain_text_to_plain_matrix worked properly
                if int_plain_matrix != None and isinstance(int_plain_matrix, list):
                    # muliply the plain text matrix with the encryption key matrix
                    int_encrypted_matrix = matrix_multiplication(int_plain_matrix, ENCRYPT_KEY_MATRIX)

        return int_encrypted_matrix
    except:
        print("Unexpected error:", sys.exc_info()[0])
