'''Testing our two translation methods'''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """Testing functionality of englishToFrench function."""
    def test1(self):
        self.assertEqual(
            english_to_french("Hello"),"Bonjour")
        self.assertEqual(
            english_to_french("Hi"),"Salut")
        self.assertEqual(
            english_to_french("school"),"école")        

class TestFrenchToEnglish(unittest.TestCase):
    """Testing functionality of frenchToEnglish function."""
    def test1(self):
        self.assertEqual(
            french_to_english("Bonjour"),"Hello")
        self.assertEqual(
            french_to_english("Salut"),"Hi")
        self.assertEqual(
            french_to_english("École"),"School")  

unittest.main()            
