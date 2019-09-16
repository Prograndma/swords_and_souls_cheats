INSTRUCTIONS FOR THIS PROGRAM
(Written by ya boi)
this program works for the game SWORDS AND SOUL	 only!!
Find it on KONGREGATE
and it only works for the STRENGTH TRAINING!!

Okay so you need to do this command in command line

# num = {your version of python}

pip install Matts\path\to\this_thing_here->\pyHook-1.5.1-cp{num}-cp{num}m-win_amd64.whl

(You also need pip installed, look it up)

Also, add python to your path (This program as it is only works on Windows)

You also need to pip a lot of things

They should be straightforward
i.e.

you might need this
pip install --upgrade pip

pip install numpy
pip install Pillow 		# you would think that it would be PIL, it's not. Lots of things are like that
pip install PyUserInput		# Only install this after you install the .whl file!!
			
			# that should be all of your pips

		   	# you have to look up how to pip each thing I import at the top of my files
		   	# you don't need to pip threading though
			# uhhhhhh
			
command to run the stuff

python capture_screen.py

# Lets see. game_cords is something that you're just going to have to 
# manually hard code because it was easier for me that way. 

Here is some code to help with that!!! (put it in your main func (near the bottom)
(after the sleep(2) command)
# You need to do this statement:
# "from PIL import Image"
|
|
real_screen = ImageGrab.grab(bbox=game_cords)
Image._show(real_screen)	
exit()		
|
|
# So look at the image and change the global variable game_cords to fix it and the program again.
# You want to write in an exit call so that you don't just start running the program
# I think game_cords[0] and [2] are actually the starting and ending y components, respectively
# You can figure out where the x_cords are. 
# obviously, comment out the above code once you're done with it. 

Once you have that figured out you can delete that code and run your program. 
Have swords and souls pulled up in chrome and running:
1. Complete the tutorial
2. Make sure that your screen is centered with 2 pixels of black surrounding it in your
   game_cords global variable
3. Start strength training, with it running before you start the program
4. Be very careful not to scroll, that will mess up the game_cords
5. run your program, (I prefer to use pycharm to do it) quickly
   jump back to chrome so it is what is showing up on the screen.
6. Your program should start working in about 2 seconds.
You're character will very likely start jumping around all crazy like
He will probably also completely miss some apples so....

# There are some globals that need to change they are:
#
# up_pixel
# left_pixel
# right_pixel
# down_pixel
#
# you need to change them like this:
#
# up, right and down _pixel need to be as high as they can possibley be without your guy going crazy
# left_pixel needs to be as low as it can possibley be without your guy kicking left constantly
# 
# each time you upgrade your room, it will change the background and change what your values
# need to be. (not every upgrade, but a lot of them)
# you'll know when your guy kicks and swings like there is no tomorrow, or just misses the apples 
# entirely. 
# You'll know things are good when you consistantly get up to combo 200+ without missing stars
# That's it! Enjoy a program that plays your video games for you. 
