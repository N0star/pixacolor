# Pixacolor
 
A simple program designed to reduce the number of colors on an uploaded image, that uses a basic machine learning algorithm.

## How to use?

1. Upload an image of your desire
2. Choose the number of iterations *(n)*
3. Choose the number of final colors *(k)*
4. **Wait till reduction is completed**
5. Show or save the final product
6. You can read info about the program whenever
7. Quit the program.
8. **Don't forget step 5. before quitting!**

## Commands

1) **U** - upload an image:
 - firstly the program will ask a user for a picture's name
 - then it will inform about the size of the image *(width x height in px)*
 - in the next step user chooses the number of loops that the program will perform *(n)*
 - and the next number to choose is the number of colors to reduce the picture to *(k)*
 - finally, the program will ask if the data is correct *(Y/n)* before taking an action
 - after that step the main loop begins - it may take some time...

2) **S** - save the reduced image:
 - perform this command only after the upload and reduction are completed
 - program will only ask for the name of the output file to save a new image
 - the output file will be automatically saved as a .png file
 - typing 'show' won't save the file, but will open its preview instead
 - this command may be used multiple times on the same picture
 
 3) **I** - show information about the program.
 4) **Q** - quit the program.
 
 ## Tips and additional info
 
 - The algorithm isn't particularly efficient - it may take some time...
 - Generally, the bigger are numbers = the more time is needed
 - Max number of colors is 256, so k>=256 is kinda pointless
 - Each iteration the program looking for a better choice of colors
 - The more iterations - the better choice, no iterations - a random choice
 - However, the quality grows logarithmically so small *n* should be enough
