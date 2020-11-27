# imports
import unittest
from matrix_encryption_helpers import (plain_text_to_plain_matrix,
plain_matrix_to_plain_text, matrix_multiplication)


class TestMatrixEncryptionHelpers(unittest.TestCase):
    # ttbm text to binary matrix conversion tests
    def test_ttbm_text_to_binary_matrix(self):
        self.assertEqual(plain_text_to_plain_matrix('Hello World!'),
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]])
    
    def test_ttbm_upper_case_string(self):
        self.assertEqual(plain_text_to_plain_matrix('HELLOWORLD'), 
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]])

    def test_ttbm_lower_case_string(self):
        self.assertEqual(plain_text_to_plain_matrix('helloworld'),
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0]])

    def test_ttbm_empty_plain_text(self):
        self.assertEqual(plain_text_to_plain_matrix(""), None)
    
    def test_ttbm_whitespace_plain_text(self):
        self.assertEqual(plain_text_to_plain_matrix("        "), None)

    def test_ttbm_non_string_input(self):
        self.assertEqual(plain_text_to_plain_matrix(['H','e','l','l','0']), None)
    
    # bmtt binary matrix to text conversion
    def test_bmtt_matrix_to_text(self):
        self.assertEqual(plain_matrix_to_plain_text(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]]), 'hello')
    
    def test_bmtt_non_matrix_input(self):
        self.assertEqual(plain_matrix_to_plain_text("hello"),None)
    
    def test_bmtt_empty_matrix_input(self):
        self.assertEqual(plain_matrix_to_plain_text([]),None)
    
    # mm is matrix multiplication
    def test_mm_matrix_multiplication(self):
        self.assertEqual(matrix_multiplication(
            [[-2,1],[0,4]],
            [[6,5],[-7,1]]),
            [[-19,-9],[-28,4]])
    
    def test_mm_empty_first_matrix_parameter(self):
        self.assertEqual(matrix_multiplication(
            [],
            [[6,5],[-7,1]]),
            None)
    
    def test_mm_empty_second_matrix_parameter(self):
        self.assertEqual(matrix_multiplication(
            [[-2,1],[0,4]],
            []),
            None)
    
    def test_mm_if_input_matrix_contains_non_numbers(self):
        self.assertEqual(matrix_multiplication(
            [[-2,1],[0,'s']],
            [[6,5],[-7,1]]),
            None)
    

if __name__ == '__main__':
    unittest.main()