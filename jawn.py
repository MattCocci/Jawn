#!/usr/bin/python

##########################################################
## Description ###########################################
##########################################################

# This script takes the first argument and
#   1.	Splits on the last period
#   2.	Looks at the file extension
#   3.	Opens with file specified in .jawn or returns error


#########################################################


import sys, os
from subprocess import Popen, PIPE, call

# Check for .jawn file in home directory
home_dir = os.environ['HOME']
home_files = os.listdir(home_dir)

if '.jawn' not in home_files:
    print "\nNo .jawn file set up in your home directory.\nSet it up with each extension-program pair on a separate line as follows:\n--------------------------------------------------------------------------\n\t[ext]=[program]\n"
    sys.exit()
else:
    # Match extensions with programs to use in a dictionary
    jawn_dict = {}
    jawn_file = open(home_dir + '/.jawn', 'r')
    for pair in jawn_file:
	ext, prog = pair.split('=')
	prog = prog.rstrip()
	jawn_dict[ext] = prog
    jawn_file.close() 


    # File to open is first argument given
    toOpen = sys.argv[1]	


    # Get the extension, where txt is the default if there is none
    if '.' in toOpen:
	ext = toOpen.split('.')[-1]
    else:
	ext = 'txt'


    # Check if there's that file extension is in the dictionary
    if ext in jawn_dict:
	toUse = jawn_dict[ext]
    else:
	print "Man, I don't know that jawn. Must not be from Philly.\nBut you could tell me about it your .jawn file so I know next time."
	sys.exit()


    # Open the file if you can
    print 'Opening that jawn\n'
    cmd = [toUse, toOpen]
    proc = call(cmd)

