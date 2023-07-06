# Python
Projects for list
Learn the append, length concept of list
● Create a Luck friend wheel application using the above concepts in tkinter.

The append() method appends an item to the end of the list.
We simply have to pass the item in this method

Syntax:
list.append(item)
Where list - existing list
item- item which needs to be added in the list.
Example :
List = [“cricket”, “basket ball”, “carrom”]
List.append(“chess”)
print(List)
Output : [“cricket”, “basket ball”, “carrom”, “chess”


We can find the length of the list by using the len() function.
len() - len() function, gives us how many items are present in the list.

Lets craete the App

Q. Why do we import * from tkinter? And how do we do that?
A. We import * from tkinter so that the tkinter library loads all the packages and methods
which are needed to create our GUI application.

Q. Why is the Tk() function used? And how do we write it?
A. We use the Tk() function to create a tkinter window on which we can place our
elements like buttons, labels, entry and make our application interactive.

Q. Which function is used to give title to the root window?
A. title() function is used to give title to the root window.

Q. Which function is used to set the dimension to the root window?
A.geometry() function

Q. What does the main loop do?
A. mainloop() makes our application executable. So it is compulsory to ad the
mainloop() at the end of the tkinter application to make the program executable.

Q. Why do we use random?
A-.We use import random to load all the methods and functions available in the
random package which are used for generating random numbers.
To import the random package we write like this.

2)   we have to take the input from the user that is the name of the friends,
we will create an entry element using the Entry() class of the tkinter.
And as we want to display it in on the root window we will pass root inside Entry()
class and assign a variable to it
3) , now we have to make this entry element visible on the root window we will use the place function().
- The place() function will align the elements as per your choice anywhere on the root window
Q - The value of relx lies between ?
A - 0.0 to 1.0

Q - Where 0.0 is and 1.0 denotes what ?
A - 0.0 Extreme left of the root window and 1.0 is extreme right of the root window.

4) Now as we have to display the list of the friends on the root window,
Now as we have to display the list of the friends on the root window,
5) Now as we have to display the generated random number on the root window,
At line 12, we create a label element using Label() 
6) Now as we have to display the name of the lucky friend on the root window,
At line 13, we create a label element using Label() class
7) At line number 15, we create a empty list as , outside the function.
We will be accessing this list inside our two functions
Since if we declare the list
Why we declare list outside function

inside our function then we will be able to use that particular list only in that
function and won't be able to use it in the other functions or outside the function
8) we declare a function to add a friend ina list 

in which it has been declared.
That’s the reason we declare an empty list outside the function.
