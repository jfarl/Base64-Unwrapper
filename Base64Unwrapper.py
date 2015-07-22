## Author: jfarl
## https://github.com/jfarl
## Copyright July 2015
## Version 1

#!/usr/bin/python
import sys
import base64

def main(argv):
	# str1 = "Wm05dkRRbz0="
	str1 = argv
	counter = 0

	print "Decoding string:",str1
	try:
		while base64.decodestring(str1):
			counter = counter + 1
			print str(counter)+':',str1
			str1 = base64.decodestring(str1)
	except:
		counter = counter + 1
		if (counter == 1):
			print "String \"" + str1 + "\" is not Bas64 encoded."
		else:
			print str(counter)+':',str1


if __name__ == "__main__":
   main(sys.argv[1])
