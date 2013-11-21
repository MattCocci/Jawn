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
    + No more accidental calls like 'vim file1.pdf' or 
	'evince file2.tex.' 
    + You specify the extension-command pairs where the command
	for a unique extension which can be arbitrarily long
	if you like to open files with a program using very
	specific settings.
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

    
	

