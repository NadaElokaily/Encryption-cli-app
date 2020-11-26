# imports
import requests
import sys
from reverse_macros import REVERSE_DENCODE_URL 

# ======================================= reverse_decryption ======================================= #
#function: reverse_decryption
#   parameters: 1, str_encoded_text(string)
#   return: 1, str_plain_text(string)
#   functionality: decrypts the input encryption text with the reverse algorithm and 
#       returns the original plain text
def reverse_decryption(str_encoded_text):
    try:
        # initialize the return
        str_plain_text = None

        # use the predefined decode url
        str_url = REVERSE_DENCODE_URL

        # specify the request payload with the 'string' item set to the str_encoded_text parameter
        dict_payload={
        "string" : str_encoded_text
        }

        # get the request response
        obj_response=requests.post(str_url,data=dict_payload)

        ## check if the response has a successful status 
        if obj_response.status_code == 200:
            # get the 'string' item from the json data in the response 
            str_plain_text = obj_response.json()['string']

        return str_plain_text  
    except:
        print("Unexpected error:", sys.exc_info()[0])
