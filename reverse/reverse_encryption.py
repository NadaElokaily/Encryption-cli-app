# imports
import requests
import sys
from reverse_macros import REVERSE_ENCODE_URL

# ======================================= reverse_encryption ======================================= #
#function: reverse_encryption
#   parameters: 1, str_plain_text(string)
#   return: 1, str_encoded_text(string)
#   functionality: encrypts the input plain text with the reverse algorithm and 
#       returns the encryption text
def reverse_encryption(str_plain_text):
    try:
        # initialize the return
        str_encoded_text = None

        # use the predefined encode url
        str_url= REVERSE_ENCODE_URL

        # specify the request payload with the 'string' item set to the str_plain_text parameter
        dict_payload={
        "string" : str_plain_text
        }

        # get the request response
        obj_response=requests.post(str_url,data=dict_payload)

        ## check if the response has a successful status 
        if obj_response.status_code == 200:
            # get the 'string' item from the json data in the response 
            str_encoded_text = obj_response.json()['string']

        return str_encoded_text 
    except:
        print("Unexpected error:", sys.exc_info()[0])
