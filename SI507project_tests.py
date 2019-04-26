import unittest
from SI507project_tools import *

class TestTools(unittest.TestCase):
    def setUp(self):
        f = open("finalproject_cache.json")
        fstr = f.read()
        f.close()
        self.states_pages = json.loads(fstr)

    def test_data_content1(self):
        self.assertTrue("MI" in self.states_pages.keys(), "Testing there is 'MI' in states")
    def test_data_content2(self):
        self.assertTrue("AL" in self.states_pages.keys(), "Testing there is 'AL' in states")
    def test_data_content3(self):
        self.assertTrue("FL" in self.states_pages.keys(), "Testing there is 'FL' in states")
    def test_MI_states_num(self):
        self.assertTrue(len(self.states_pages['MI'])>1, "Testing if there exists more than one park in MI")
    def test_AL_states_num(self):
        self.assertEqual(len(self.states_pages['AL'])>1, "Testing if there are enough parks in AL")
    def test_FL_states_num(self):
        self.assertEqual(len(self.states_pages['FL'])>1, "Testing if there are enough parks in FL")
    def test_items_in_AL_states_num(self):
        self.assertEqual(len(self.states_pages['AL'][list(self.states_pages['AL'].keys())[0]]),2, "Testing if there are enough items in AL states")
    def test_items_in_ML_states_num(self):
        self.assertEqual(len(self.states_pages['ML'][list(self.states_pages['ML'].keys())[0]]),2, "Testing if there are enough items in ML states")
    def test_items_in_FL_states_num(self):
        self.assertEqual(len(self.states_pages['FL'][list(self.states_pages['FL'].keys())[0]]),2, "Testing if there are enough items in FL states")

if __name__ == "__main__":
    unittest.main(verbosity=2)
