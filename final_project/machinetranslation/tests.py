import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrechToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
