import unittest
from SI507project_code import *

class TestTools(unittest.TestCase):
    def setUp(self):
        f = open("finalproject_cache.json")
        fstr = f.read()
        f.close()
        self.states_pages = state_list
        self.states_type = type_list
        self.description = description_list


    def test_data_content1(self):
        self.assertTrue("MI" in self.states_pages, "Testing there is 'MI' in states")
    def test_data_content2(self):
        self.assertTrue("AL" in self.states_pages, "Testing there is 'AL' in states")
    def test_data_content3(self):
        self.assertTrue("FL" in self.states_pages, "Testing there is 'FL' in states")
    def test_NM_content(self):
        self.assertTrue('National Monument' in self.states_type, "Testing there is 'National Monument' in type")
    def test_NCT_content(self):
        self.assertTrue('National Scenic Trail' in self.states_type, "Testing there is 'National Scenic Trail' in type")
    def test_NHT_content(self):
        self.assertTrue('National Historic Trail' in self.states_type, "Testing there is 'National Historic Trail' in type")
    def test_length_in_description(self):
        self.assertTrue(len(self.description[1])>20, "Testing if there are enough words in description")

if __name__ == "__main__":
    unittest.main(verbosity=2)
