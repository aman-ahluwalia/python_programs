import urllib

def check_for_profanity():
	particular_file = open("file_path/file_name.txt")
	contents_of_file = particular_file.read()
	print(contents_of_file)
	particular_file.close()
	check_contents_for_parity(contents_of_file)

def check_contents_for_parity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
	output = connection.read()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan scan the document properly!")
	connection.close()

check_for_profanity()