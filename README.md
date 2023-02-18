# FakeNumbers
Generate fake numbers! Currently the script only generates the numbers one and two, and I am not exactly sure if I will add the other numbers 
into the script, as the main benefit for writing the program was to familiarize myself with the PIL library, as well as some basics of computer 
graphics.

I built the progect using the Pillows, Scipy, and Numpy to help with some of the math and such. The rest of the functions like the ability to drawing lines
were implemented in by me, and they definetly are not the most efficent or best out there. Pillows has good line drawing functionality already, but
again the reason for this program was to familiarize myself with the ways to do that myself, instead of using pre-existing functionality. 

I got the inspiration for this program based on the MNIST hand written numbers dataset, as I wanted to see if it was possible to generate my own numbers that were
like the MNIST data, and train a basic neural net to see if it worked. After generating the ones and two, I found that in supplement to the 
already existing MNIST data sets, the fake numbers I generated did just as well as the regular MNIST data set, and I speculate that with the ability
to generate a full range of numbers and fix some of the issues with the current code, that the fake numbers could be just as effective to training a 
nerual net to identifying hand written numbers. 

Through the project, I learned about the different algorithms to drawing lines in 2D like the DDA algorithm, which I tweaked slightly in the drawLine method
to make it more accurate, as the regular DDA algorithm wasn't 100% accurate at drawing lines exactly where they should be. That was an issue, as there would
be gaps between the lines, but with the slight tweak I made it work everytime. 

I also learned some basics of Scipy, Numpy, Pillows, and got better at programming with Python. 
