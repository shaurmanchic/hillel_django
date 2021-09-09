import unittest

class TestUtilDate(unittest.TestCase):
    def setUp(self):
        #init_something()
        pass
        
    def tearDown(self):
        #teardown_something()
        pass
        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        
    def test_failed_upper(self):
        self.assertEqual('foo'.upper(), 'FOo')