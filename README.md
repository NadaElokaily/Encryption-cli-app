# Encryption CLI APP

The Encryption command line tool is a tool that can provide the encryption and decryption representation for any string received from the user using some pre-defined algorithms

## the Main Tasks:
the tool can encrypt and decrypt string for the following algorithms:
1) Shift Algorithm aka Ceaser Cipher
2) Matrix Algorithm
3) Reverse Algorithm

## Dependencies

### Installing Dependencies

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

## File Structure
app\
├──src\
│     ├──ceaser\
│     │     ├──ceaser_encryption.py\
│     │     ├──ceaser_decryption.py\
│     │     └──shift_test.py\
│     ├──matrix\
│     │     ├──matrix_macros.py\
│     │     ├──matrix_encryption_helpers.py\
│     │     ├──matrix_encryption.py\
│     │     ├──matrix_decryption.py\
│     │     ├──matrix_test.py\
│     │     └──matrix_helpers_test.py\
│     ├──reverse\
│     │     ├──reverse_macros.py\
│     │     ├──reverse_encryption.py\
│     │     └──reverse_decryption.py\
│     └──encryption_tool.py\
├── Dockerfile\
└──README.md\

## Tool 
    the main command line tool resides in /app/encryption_tool.py

## Testing
To run the tests, run
```
python ceaser\shift_test.py
python matrix\matrix_test.py
python matrix\matrix_helpers_test.py
```

## Encryption Tool
the tool exists in the encryption_tool.py to run the tool simply use the command
```
python encryption_tool.py
```
first user'll be greated with a msg like this to enter the input text
#### Please type the desired text
then the tool will ask to specify the desired algorithm

#### Please enter 'shift', 'matrix', 'reverse' or (s/m/r) to pick the desired algorithm name
user can enter:
[s or shift (upper or lower case)] for the shift algorithm,
[m or matrix (upper or lower case)] for the matrix algorithm,
[r or reverse (upper or lower case)] for the reverse algorithm
any other input would be discarded and user will be asked to re-choose the desired algorithm

then the tool would ask for the action type 

#### Please type 'encrypt', 'decrypt' or (e/d) to pick the required action
user can enter:
[e or encrypt (upper or lower case)] for Encryption,
[d or decrypt (upper or lower case)] for Decryption
any other input would be discarded and user will be asked to re-choose the desired action

then the tool would then display the result

#### the result is ****
then the tool would ask if the user wants to exit

#### Do you want to exit program? y/n
user can enter:
[y or Y] to exit,
[n or N] to continue


## Sample encryption input case
```
please type the desired text
Hello World
please enter 'shift', 'matrix', 'reverse' or (s/m/r) to pick the desired algorithm name
s
please type 'encrypt', 'decrypt' or (e/d) to pick the required action
e
please enter the shift amount
3
the result is Khoor Zruog
do you want to exit program? y/n
```

## Sample decryption input case
```
please type the desired text
[[15, 12, 12, 14, 15, 15, 14, 9, 6, 14, 12, 8, 8, 20, 17, 5], [18, 19, 5, 22, 8, 13, 14, 10, 5, 22, 20, 20, 18, 27, 20, 12], [19, 14, 13, 21, 15, 17, 21, 18, 8, 22, 17, 15, 14, 27, 18, 14], [19, 14, 13, 21, 15, 17, 21, 18, 8, 22, 17, 15, 14, 27, 18, 14], [28, 25, 18, 27, 26, 24, 28, 20, 10, 36, 25, 21, 29, 43, 28, 16], [6, 6, 0, 7, 2, 7, 1, 0, 2, 6, 4, 2, 2, 9, 4, 0], [31, 28, 16, 27, 18, 22, 21, 12, 16, 33, 27, 29, 27, 40, 29, 14], [28, 25, 18, 27, 26, 24, 28, 20, 10, 36, 25, 21, 29, 43, 28, 16], [22, 17, 14, 16, 16, 17, 13, 3, 14, 17, 17, 16, 12, 24, 21, 5], [19, 14, 13, 21, 15, 17, 21, 18, 8, 22, 17, 15, 14, 27, 18, 14], [13, 10, 4, 18, 6, 10, 13, 10, 5, 14, 15, 14, 9, 18, 13, 12]]
please enter 'shift', 'matrix', 'reverse' or (s/m/r) to pick the desired algorithm name
m
please type 'encrypt', 'decrypt' or (e/d) to pick the required action
d
the result is hello world
do you want to exit program? y/n
```

### extra notes 
make sure the text input for the matrix decryption doesn't contain new lines

## Algorithms
### Shift Algorithm
shifts every character in the string by provided integer shift amount


### Matrix Algorithm
Convert each character of the string to the Binary representation of ASCII character (16
characters) then multiplies the resultant matrix with the ENCRYPT_KEY_MATRIX to return the final encrypted matrix


### Reverse Algorithm
reverses the given string using functions remotely implemented using the endpoints:
● Encryption : http://backendtask.robustastudio.com/encode
● Decryption : http://backendtask.robustastudio.com/decode


## Methods

### function: ceaser_encryption
####   parameters: 
2, str_plain_text(string), int_shift(integer)
####   return: 
1, encrypted_text(string)
####   functionality: 
encrypts the input plain text with the shift algorithm and returns the encrypted text


### function: ceaser_decryption
####   parameters: 
2, str_encrypted_text(string), int_shift(integer)
####   return: 
1, plain_text(string)
####   functionality: 
decrypts the input encryption text with the shift algorithm and returns the original plain text


### function: matrix_encryption
####   parameters: 
1, str_plain_text(string)
####   return: 
1, int_encrypted_matrix(array of integers)
####   functionality: 
encrypts plain text with the matrix and returns the encrypted resultant matrix

### function: matrix_decryption
####   parameters: 
1, int_encrypted_matrix(array of integers)
####   return: 
1, str_plain_text(string)
####   functionality: 
decrypts the encrypted matrix with the matrix algorithm and returns plain text


### function: plain_text_to_plain_matrix
####   parameters: 
1, str_plain_text(string)
####   return: 
1, int_plain_matrix(array of integers)
####   functionality: 
takes each plain text character and changes it to a 16 items list equivalent to the binary representation of its ascii value then returns the resultant plain text matrix for all characters in the input plain text


### function: plain_matrix_to_plain_text
####   parameters: 
1, int_plain_matrix(array of integers)
####   return: 
1, str_plain_text(string)
####   functionality: 
takes the binary representation of its ascii value for each plain text character and gets the equivalent  character then returns the plain text string


### function: matrix_multiplication
####   parameters: 
2, int_plain_matrix(array of integers), int_key_matrix(array of integers)
####   return: 
1, int_result_matrix(array of integers)
####   functionality: 
muliplies the 2 input matricies and returns a resultant matrix output


### function: reverse_encryption
####   parameters: 
1, str_plain_text(string)
####   return: 
1, str_encoded_text(string)
####   functionality: 
encrypts the input plain text with the reverse algorithm and returns the encryption text


### function: reverse_decryption
####   parameters: 
1, str_encoded_text(string)
####   return: 
1, str_plain_text(string)
####   functionality: 
decrypts the input encryption text with the reverse algorithm and returns the original plain text


### function: get_non_empty_valid_string_field
####   parameters: 
2, str_type(string), str_accepted_vals_list(list of strings)
####   return: 
1, str_input_value(string)
####  functionality: 
loop over the value inputed by user till it reaches a valid value that is in the str_accepted_vals_list


### function: get_non_empty_valid_int_field
####   parameters: 
0, No parameters
####   return: 
1, int_integer_value(integer)
####   functionality: 
loop over the value inputed by user till then user inputs a valid integer value


### function: encryption_tool
####   parameters: 
0, No parameters
####   return: 
0, No return
####   functionality: 
runs the cli tool for encrypting and decrypting text passed by the user with the desired algorithm
