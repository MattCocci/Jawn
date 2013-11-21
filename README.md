Jawn
====

For opening any jawn you want from the command line.


Basic Idea
-----------

Open a file with any extension---that is, open any jawn---simply
with

    j file.ext

Like a file launcher, just tell jawn what file you want to open,
and it will open with the correct program (which you specify
in a .jawn file). 

    + No more accidental calls like 'vim file1.pdf' or 'evince file2.tex.' 
    + You specify the extension-command pairs where the   
    	command for a unique extension which can be arbitrarily 
    	long if you like to open files with a program using very specific settings.
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

at the command line, the file is open with command 'cmd' from your
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
    sh install.sh
	
This will write a default .jawn file in your home directory, then 
add a new function to your .bashrc in your home folder. The function
(and thus jawn itself) is exucuted by typing at the command line
    
    j jawn

The function j then

    1.	Checks if jawn is a directory. If so, cd into that directory.
    2.	If jawn is a regular file, execute  
    		
    		python INSTALL_DIR_PATH/jawn.py jawn 
    		
    	which will check jawn for an extension and open it with the program specified in ~/.jawn (if it finds one). 


Note that "INSTALL\_DIR\_PATH" is the path of the directory you cloned. 
If ever move jawn.py, you'll have to change the path in the body of 
the j() function that was written to your .bashrc. 

