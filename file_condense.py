import os
import sys
"""
This is a very basic python script 
is used to demonstrate using CI

Functionally it just condenses all files in a directory into one,
	yes there are better ways to do this.
"""


def extract_all_file_contents(folder, type_exclusions):
	"""
	Given a folder to start with extract all
	file contents recursively as long as the 
	file is not of a type in exclusions
	"""	
	contents = ''
	for folder, _, files in os.walk(folder):
		for file in files:
			if not file.endswith(type_exclusions):
				file_path = os.path.join(folder, file)
				with open(file_path, 'rb') as input_file:
					contents += input_file.read().decode('utf-8') + '\n' 
	return contents

if __name__ == "__main__" and len(sys.argv) >= 2:
	print(len(sys.argv))
	folder = sys.argv[1]
	output_file = sys.argv[2]
	type_exclusions = ()
	if len(sys.argv) > 3:
		type_exclusions = tuple(sys.argv[3:])
	file_contents = extract_all_file_contents(folder, type_exclusions)
	with open(output_file, 'wb') as condensed_file:
		condensed_file.write(file_contents.encode('utf-8'))
