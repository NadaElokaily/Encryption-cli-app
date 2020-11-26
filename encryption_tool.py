# imports
import sys
from ceaser.ceaser_encryption import ceaser_encryption
from ceaser.ceaser_decryption import ceaser_decryption
from matrix.matrix_encryption import matrix_encryption
from matrix.matrix_decryption import matrix_decryption_text

# ======================== get_non_empty_valid_string_field ======================== #
#function: get_non_empty_valid_string_field
#   parameters: 2, str_type(string), str_accepted_vals_list(list of strings)
#   return: 1, str_input_value(string)
#   functionality: loop over the value inputed by user till it reaches a valid value that
#       is in the str_accepted_vals_list
def get_non_empty_valid_string_field(str_type, str_accepted_vals_list):
    try:
        str_input_value = ""

        # loop over the str_input_value if the user typed invalid algorithm
        # name other than shift or matrix 
        while (str_input_value not in str_accepted_vals_list):
            # check if this isn't the first loop iteration
            if str_input_value != "":
                print('Not a valid choice\n')
                
            # get the algorithm type
            if str_type == 'algorithm':
                str_input_value = input("please enter 'shift', 'matrix' or (s/m) to pick the desired algorithm name\n").lower().replace(" ","")
            # get the action type
            elif str_type == 'action':
                str_input_value = input("please type 'encrypt', 'decrypt' or (e/d) to pick the required action\n").lower().replace(" ","")
    
        return str_input_value
    except:
        print("Unexpected error:", sys.exc_info()[0])


# better function for checking if str contains positive and negative numbers
def is_digit(str_number):
    try:
        int(str_number)
        return True
    except ValueError:
        return  False

# ======================== get_non_empty_valid_int_field ======================== #
#function: get_non_empty_valid_int_field
#   parameters: 0, No parameters
#   return: 1, int_integer_value(integer)
#   functionality: loop over the value inputed by user till then user inputs a valid integer value
def get_non_empty_valid_int_field():    
    try:
        str_integer_value = ""
        # loop till the user inputs a valid integer shift amount
        while not is_digit(str_integer_value):
            # check if this isn't the first loop iteration
            if str_integer_value != "":
                print('Not a valid choice only integers\n')
            
            # get input from user
            str_integer_value = input('please enter the shift amount\n')

        # change the syring value attained from the terminal into integer 
        int_integer_value = int(str_integer_value) 
        return int_integer_value
    except:
        print("Unexpected error:", sys.exc_info()[0])


# ======================== encryption_tool ======================== #
#function: encryption_tool
#   parameters: 0, No parameters
#   return: 0, No return
#   functionality: runs the cli tool for encrypting and decrypting text 
#       passed by the user with the desired algorithm
def encryption_tool():
    while(True):
        # initialize the output
        str_result = ""
        # take the input text from the terminal
        str_input_text = input("please type the desired text\n")
    
        # get valid value from terminal for the algorithm type
        str_algorithm_type = get_non_empty_valid_string_field('algorithm', 
        ['shift','s','matrix','m'])

        # get valid value from terminal for the action type
        str_action_type = get_non_empty_valid_string_field('action', ['decrypt', 'd', 'encrypt', 'e'])  
        
        # check the selected algorithm
        if str_algorithm_type in ['shift','s']:
            # get a vaild int shift amount from the terminal
            int_shift_amount = get_non_empty_valid_int_field()
            # perform encryption or decryption as the user required
            if str_action_type in ['encrypt','e']:
                str_result = ceaser_encryption(str_input_text,int_shift_amount)
            elif str_action_type in ['decrypt','d']:
                str_result = ceaser_decryption(str_input_text,int_shift_amount)

        elif str_algorithm_type in ['matrix','m']:
            if str_action_type in ['encrypt','e']:
                str_result = str(matrix_encryption(str_input_text))
            elif str_action_type in ['decrypt','d']:
                str_result = matrix_decryption_text(str_input_text)     
        print(('the result is {r}').format(r=str_result))
        
        # ensure that the user doesn't want to exit the program
        str_exit = input('do you want to exit program? y/n\n')
        if str_exit in ['y','Y']:
            break
    return

if __name__ == "__main__":
    encryption_tool()
