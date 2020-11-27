# imports
from matrix_macros import DECRYPT_KEY_MATRIX
from matrix_encryption_helpers import matrix_multiplication, plain_matrix_to_plain_text
import sys
import ast

# ======================================= matrix_decryption ======================================= #
#function: matrix_decryption
#   parameters: 1, int_encrypted_matrix(array of integers)
#   return: 1, str_plain_text(string)
#   functionality: decrypts the encrypted matrix and returns plain text
def matrix_decryption(int_encrypted_matrix):
    try:
        # initize return value
        str_plain_text = None 
        # check if input matrix is not empty and is a list
        if int_encrypted_matrix and isinstance(int_encrypted_matrix,list):
            # muliply the encrypted matrix with the decryption key matrix to get the decrypted matrix
            int_decrypted_matrix = matrix_multiplication(int_encrypted_matrix, DECRYPT_KEY_MATRIX)

            # check if the matrix_multiplication returned a valid matrix list
            if int_decrypted_matrix != None and isinstance(int_decrypted_matrix,list): 
                # get the plain text 
                str_plain_text = plain_matrix_to_plain_text(int_decrypted_matrix)
        return str_plain_text
    except:
        print("Unexpected error:", sys.exc_info()[0])

def matrix_decryption_text(str_encrypted_text):
    # convert the string entered to a list of lists of string items
    str_encrypted_list = ast.literal_eval(str_encrypted_text)
    # convert the string items to integers
    int_encrypted_matrix = [[int(i) for i in r] for r in str_encrypted_list]
    # call the decryption function with the obtained value
    return matrix_decryption(int_encrypted_matrix)


