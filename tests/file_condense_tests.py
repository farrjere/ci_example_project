import unittest
from ci_example_project import file_condense as fc

class FileCondenseTests(unittest.TestCase):
	def test_no_folder(self):
		contents = fc.extract_all_file_contents('non_existent', ())
		self.assertEquals('', contents)

	def test_simple_read(self):
		contents = fc.extract_all_file_contents('tests/examples', ())
		self.assertTrue('Another' in contents)
		self.assertTrue('file' in contents)

	def test_nested_read(self):
		contents = fc.extract_all_file_contents('tests/nested', ())
		self.assertTrue('1' in contents)
		self.assertTrue('2' in contents)