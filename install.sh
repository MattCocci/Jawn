#!/bin/sh

###########################################################
## Description ############################################
###########################################################

# If you run sh install.sh at the command line,
#
#   1.	A .jawn file is initialized in the home directory
#	with default extension-command pairs.
#
#   2.	Adds an alias to your .bashrc so that you can
#	use 
#		j file.ext
#
#	rather than 
#
#		python jawn.py file


###########################################################

# Make a default .jawn file in the home directory
echo "Writing default .jawn file to home directory..."
printf "pdf=evince\neps=evince\ntxt=vim\nsh=vim" > "$HOME/.jawn"

# Should chmod jawn.py
echo "Making jawn.py and jawn_cd.sh executable..."
chmod +x jawn.py

## Add function to .bashrc
echo "Adding j function to .bashrc..."
printf "\nfunction j()"			    >> ~/.bashrc 
printf "\n{"				    >> ~/.bashrc 
printf '\n	if [ -d $1 ]'		    >> ~/.bashrc 
printf '\n	then '			    >> ~/.bashrc 
printf '\n	    cd $1'		    >> ~/.bashrc 
printf '\n	else '			    >> ~/.bashrc 
printf "\n	    python $PWD/jawn.py"    >> ~/.bashrc 
printf ' $1'				    >> ~/.bashrc 
printf '\n	fi'			    >> ~/.bashrc 
printf '\n}'				    >> ~/.bashrc 
#echo "alias j='python $PWD/jawn.py'" >> $HOME/.bashrc



# Conclusion
printf "\n"
printf "A .jawn jawn is set up in your home jawn.\nGo specify some new extension-command pairs, placing each unique pair on a new line in the form 'ext=cmd'.\n"
printf "\n"




