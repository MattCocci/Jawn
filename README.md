Jawn
====

jawn *noun*: A word used by Philly cats to describe anything and everything.
--Urban Dictionary

As you might guess, this program is for opening any jawn you want 
from the command line.


Basic Idea
-----------

Open a file with any extension---that is, open any jawn---simply
with

    j file.ext

Like a file launcher, just tell jawn what file you want to open,
and it will open with the correct program (which you specify
in a .jawn file). 

+ No more accidental calls like 'vim file1.pdf' or 'evince file2.tex.' 
+ You specify the extension-command pairs. Note the command for a unique extension can be arbitrarily long,  in case you like to open files using very specific settings with a program .
+ You hardly have to move since jawn uses a home key.


How it Works
--------------

In your home directory, set up a .jawn file. The installation
instructions below will set up defaults, but you're free to modify
and add.  

Each line in the .jawn file specifies an extension-command pair as

    ext=cmd

Then, when you type 
    
    j file.ext

at the command line, the file is opened with command 'cmd' from your
.jawn file.

And if you happen to type
    
    j dir

where dir is some directory, you'll cd into that directory.

    
Installation
-------------

Navigate to a location where you can store the executable. It could be
your /usr/bin folder, or any folder on your machine. Then

    git clone https://github.com/mcocci/Jawn.git

Then
    
    cd Jawn
    chmod +x install.sh
    sh install.sh
	
This will write a default .jawn file in your home directory, then 
add a new function to your .bashrc in your home folder. The function
(and thus jawn itself) is exucuted by typing at the command line
    
    j jawn

All you need to do is restart your shell jawn, then you can
open any jawn.


Installation Note
-------------------

The function j proceeds as follows, when executed with the argument 'jawn':

1.	Checks if jawn is a directory. If so, cd into that directory.
2.	If jawn is a regular file, execute  
    		
    		python INSTALL_DIR_PATH/jawn.py jawn 
    		
	which will check jawn for an extension and open it with the program specified in ~/.jawn (if it finds one). 


Note that "INSTALL\_DIR\_PATH" is the path of the directory you cloned. 
If ever move jawn.py, you'll have to change the path in the body of 
the j() function that was written to your .bashrc. 

