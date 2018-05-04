import os
import unittest
import urllib3
import filecmp
from generate_neighbourhoods import generate_neighbourhoods

file_path1 = "../html/js/ranked_price.js"
file_path2 = "../html/js/ranked_rating.js"
file_path3 = "../html/js/neighbourhoods.json"
file_path4 = "../html/js/neighbourhoods.js"
target_file1 = "files/ranked_price.js"
target_file2 = "files/ranked_rating.js"
target_file3 = "files/neighbourhoods.json"
target_file4 = "files/neighbourhoods.js"

class TestCase(unittest.TestCase):
    # case: if file1 is present under path
    def test_file_exist1(self):
        generate_neighbourhoods()
        is_exist = os.path.exists(file_path1)
        self.assertTrue(is_exist)

    # case: if file2 is present under path
    def test_file_exist2(self):
        generate_neighbourhoods()
        is_exist = os.path.exists(file_path2)
        self.assertTrue(is_exist)

	# case: if file3 is present under path
    def test_file_exist3(self):
        generate_neighbourhoods()
        is_exist = os.path.exists(file_path3)
        self.assertTrue(is_exist)

    # case: if file3 is present under path
    def test_file_exist4(self):
        generate_neighbourhoods()
        is_exist = os.path.exists(file_path4)
        self.assertTrue(is_exist)

    # case: if file1 is identical as target file
    def test_file_identity1(self):
        self.assertTrue(filecmp.cmp(file_path1, target_file1))

    # case: if file2 is identical as target file
    def test_file_identity2(self):
        self.assertTrue(filecmp.cmp(file_path2, target_file2))

    # case: if file3 is identical as target file
    def test_file_identity3(self):
        self.assertTrue(filecmp.cmp(file_path3, target_file3))

    # case: if file4 is identical as target file
    def test_file_identity4(self):
        self.assertTrue(filecmp.cmp(file_path4, target_file4))


if __name__ == '__main__':
    unittest.main()