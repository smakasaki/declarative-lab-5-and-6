import unittest
import os
import zip_module


class TestZipModule(unittest.TestCase):

    def setUp(self):
        self.test_file1 = "test_file1.txt"
        self.test_file2 = "test_file2.txt"
        with open(self.test_file1, "w") as f:
            f.write("This is a test file.")
        with open(self.test_file2, "w") as f:
            f.write("This is another test file.")

    def tearDown(self):
        os.remove(self.test_file1)
        os.remove(self.test_file2)
        if os.path.exists("test.zip"):
            os.remove("test.zip")

    def test_create_zip(self):
        result = zip_module.create_zip(
            [self.test_file1, self.test_file2], "test.zip")
        self.assertTrue(result)
        self.assertTrue(os.path.exists("test.zip"))

    def test_extract_zip(self):
        zip_module.create_zip([self.test_file1, self.test_file2], "test.zip")
        result = zip_module.extract_zip("test.zip", ".")
        self.assertTrue(result)

    def test_add_file_to_zip(self):
        zip_module.create_zip([self.test_file1], "test.zip")
        result = zip_module.add_file_to_zip("test.zip", self.test_file2)
        self.assertTrue(result)
        files_in_zip = zip_module.list_files_in_zip("test.zip")
        self.assertIn(self.test_file2, files_in_zip)

    def test_list_files_in_zip(self):
        zip_module.create_zip([self.test_file1, self.test_file2], "test.zip")
        files_in_zip = zip_module.list_files_in_zip("test.zip")
        self.assertIn(self.test_file1, files_in_zip)
        self.assertIn(self.test_file2, files_in_zip)


if __name__ == "__main__":
    print(zip_module.__doc__)
    unittest.main()
