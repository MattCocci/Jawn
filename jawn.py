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



# Check that there's a .jawn file in the home directory
if '.jawn' not in home_files:
  print '\nNo .jawn file set up in your home directory.'
  print '\nSet it up with each extension-program pair on a separate line as follows:'
  print '\n--------------------------------------------------------------------------'
  print '\n\t[ext]=[program]\n'
  sys.exit()

# If you've got a .jawn file set up
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

  # If file does not exist, prompt whether to create or break jawn execution
  if not os.path.isfile(toOpen):
    create = raw_input('Create file ' + toOpen + '? [y to create]: ')
    if create == 'y':
      open(toOpen, 'a').close()
    else:
      sys.exit()
      
  # Get the extension, where txt is the default if there is none
  default = 'txt'
  if '.' not in toOpen:
      ext = default

  else:
    # Split on pathbreaks take the end of the path
    toOpen_split = toOpen.split('/')[-1]

    # Split on the pd
    toOpen_split = toOpen_split.split('.')

    # Check if you're opening a dotfile like .bashrc or .vimrc
    if not toOpen_split[0]:
      ext = default
    else:
      # Grab the extension
      ext = toOpen.split('.')[-1]

    # Check if that file extension is in the dictionary
    if ext in jawn_dict:
      toUse = jawn_dict[ext]
      toUse = toUse.split()
    else:
      print 'Man, I don''t know that jawn you gave me, ' + ext
      print '\nMust not be from Philly.'
      print '\nBut you could tell me about it in your ~/.jawn file so I know next time.'
      sys.exit()

    # Open the file if you can
    toUse.append(toOpen)
    proc = call(toUse)

