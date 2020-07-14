#14th July Project Status Update 1

##The Problem
My first significant challenge roadblock in the development of the terminal application was combining the timer function with the user input function, which should reset the timer.
My application requires that the timer reset itself whenever there is user input, however, because python does not run all code simultaneously, my loop and user input will preclude 
one another from starting before the other has finished. For example, in pseudo code:


###Situation a)
while timer is above 0:
    subtract 1 each second

user input:
    reset timer


*This will not work because the timer will reach 0, exiting the while loop, and only then ask the user for input. If instead we flip this the other way:

###Situation b)
user input:
    reset timer

while timer is above 0:
    subtract 1 each second


*Python will not start the loop until the user has supplied input, and after input is given. It is important for the user to be able to feed input into the application while the timer is running


##Solution

The solution to this problem was to learn a new concept, threading. Threading is a process that allows the program to continue reading while one part is 'waiting'.
For example, while python 'waits' for user input, it will continue onward to read other parts of the code simultaneously. 


