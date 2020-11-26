# imports
import unittest
from ceaser_encryption import ceaser_encryption

class TestCeaserEncryption(unittest.TestCase):
    
    def test_upper_case_string(self):
        self.assertEqual(ceaser_encryption('HELLOWORLD',3), 'KHOORZRUOG')

    def test_lower_case_string(self):
        self.assertEqual(ceaser_encryption('helloworld',3), 'khoorzruog')

    def test_upper_and_lower_case_string(self):
        self.assertEqual(ceaser_encryption('HelloWorld',3), 'KhoorZruog')
    
    def test_spaces_and_characters_within_string(self):
        self.assertEqual(ceaser_encryption('Hello World !',3), 'Khoor Zruog !')
        
    def test_empty_plain_text(self):
        self.assertEqual(ceaser_encryption("",3), None)

    def test_whitespace_plain_text(self):
        self.assertEqual(ceaser_encryption("        ",3), None)

    def test_non_string_input(self):
        self.assertEqual(ceaser_encryption(['H','e','l','l','0'],3), None)

    def test_non_integer_shift(self):
        self.assertEqual(ceaser_encryption('Hello World!','3'), None)
    
    def test_negative_shift(self):
        self.assertEqual(ceaser_encryption('Khoor Zruog!',-3), 'Hello World!')

    def test_very_large_shift(self):
        self.assertEqual(ceaser_encryption('Hello World!',55),'Khoor Zruog!')

    def test_no_shift(self):
        self.assertEqual(ceaser_encryption('Hello World!',0),'Hello World!')

if __name__ == '__main__':
    unittest.main()