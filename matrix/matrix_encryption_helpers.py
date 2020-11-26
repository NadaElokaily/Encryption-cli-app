# imports
import sys


# ======================================= plain_text_to_plain_matrix ======================================= #
#function: plain_text_to_plain_matrix
#   parameters: 1, str_plain_text(string)
#   return: 1, int_plain_matrix(array of integers)
#   functionality: takes each plain text character and changes it to a 16 items list 
#       equivalent to the binary representation of its ascii value then returns the resultant plain text
#       matrix for all characters in the input plain text
def plain_text_to_plain_matrix(str_plain_text):
    try:
        # initialize the return
        int_plain_matrix = None
        # check if the input plain text is not empty or filled with white space 
        if isinstance(str_plain_text,str):
            if str_plain_text.strip():
                int_plain_matrix = []

                ## loop through all the plain text characters
                for char_c in str_plain_text:                              
                    ## put the character on the 16 item binary representation list
                    # ord(char_c) to get the ascii value of the character
                    int_ascii_value = ord(char_c)
                    # bin(int_ascii_value) to get the binary representation of the ascii value as a string 
                    # [2:] to remove the 0b that results from the bin function
                    str_binary_ascii = bin(int_ascii_value)[2:]
                    # zfill(16) to add leading zeros if the order of the binary value if less than 16
                    str_binary_ascii_16 = str_binary_ascii.zfill(16)
                    # create a list with the 16 characters as integers for multiplication 
                    int_c_binary_list = [int(i) for i in str_binary_ascii_16]

                    ### NOTE: we could have eliminated the local variables and used the formula  
                    ### [int(i) for i in (bin(ord(char_c))[2:].zfill(16))] but it is harder to 
                    ### read, comprehend and maintain

                    # push the character binary list items to the matrix
                    int_plain_matrix.append(int_c_binary_list)

        return int_plain_matrix
    except:
        print("Unexpected error:", sys.exc_info()[0])


# ======================================= plain_matrix_to_plain_text ======================================= #
#function: plain_matrix_to_plain_text
#   parameters: 1, int_plain_matrix(array of integers)
#   return: 1, str_plain_text(string)
#   functionality: takes the binary representation of its ascii value for each plain text character and
#       gets the equivalent  character then returns the plain text string
def plain_matrix_to_plain_text(int_plain_matrix):
    try:
        # initialize the return
        str_plain_text = None
        if isinstance(int_plain_matrix,list):
            # check if plain_matrix is not empty
            if int_plain_matrix:
                str_plain_text = ""

                ## loop through all the plain text characters
                for row in int_plain_matrix:
                    str_binary_ascii = "".join(str(x) for x in row)
                    # get the integer value equivalen to the binary value(base 2)
                    int_ascii_value = int(str_binary_ascii,2)
                    # get the character equivalent to the int ascii value & append it to the result string
                    str_plain_text += chr(int_ascii_value)

        return str_plain_text
    except:
        print("Unexpected error:", sys.exc_info()[0])


# ======================================= matrix_multiplication ======================================= #
#function: matrix_multiplication
#   parameters: 2, int_plain_matrix(array of integers), int_key_matrix(array of integers)
#   return: 1, int_result_matrix(array of integers)
#   functionality: muliplies the 2 input matricies and returns a resultant matrix output
def matrix_multiplication(int_plain_matrix, int_key_matrix):
    try :
        int_result_matrix = None
        # check if input matrices are not empty and are lists
        if int_plain_matrix and isinstance(int_plain_matrix, list) and int_key_matrix and isinstance(int_key_matrix, list):
            # check if the number of columns of the int_plain_matrix = the number of rows of the int_key_matrix
            if len(int_plain_matrix[0]) == len(int_key_matrix):            
                int_result_matrix = [] 

                ## looping over the rows of the int_plain_matrix 
                for i in range(len(int_plain_matrix)):    
                    int_result_row_list = []

                    ## looping over the coloums of the int_key_matrix  
                    for j in range(len(int_key_matrix[0])):    
                        int_result_item = 0 
                        
                        ## looping over the rowss of the int_key_matrix 
                        for k in range(len(int_key_matrix)): 

                            # check if the two multiplicated items are valid integers or floats
                            if (( isinstance(int_plain_matrix[i][k], int) or isinstance(int_plain_matrix[i][k], float) )
                            and ( isinstance(int_key_matrix[k][j], int) or isinstance(int_key_matrix[k][j], float) )):
                                # adding the int_result_matrix of the product to the item in the int_result_matrix
                                int_result_item += int_plain_matrix[i][k] * int_key_matrix[k][j] 
                            else:
                                return None

                        # append single items to int_result_matrix row
                        int_result_row_list.append(round(int_result_item))

                    # appending rows to the int_result_matrix matrix
                    int_result_matrix.append(int_result_row_list)

        return int_result_matrix
    except:
        print("Unexpected error:", sys.exc_info()[0])
    