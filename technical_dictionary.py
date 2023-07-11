from tkinter import *
root=Tk()
root.geometry("600x400")
root.configure(background='orange')
root.title("Dictionary")

label_of_mutable = Label(root)
label_of_immutable = Label(root)
label_of_tkinter = Label(root)

dictionary = {'Mutable': 'Values can be changed just like a List',
              'Immutable': 'Values can not be changed  just like a tuple',
              'Tkinter': 'It is the GUI library of python'}

def mutable():
    label_of_mutable["text"] = dictionary['Mutable']# Define first function to access the meaning of mutable.
    
def immutable():
    label_of_immutable["text"] = dictionary['Immutable'] #Define second function to access the meaning of immutable.

#Define third function to access the meaning of tkinter.    
def tkinter():
    label_of_tkinter["text"] = dictionary['Tkinter']
    
button_mutable= Button(root, text = "Meaning of Mutable",command = mutable)# Create first button to call a function to display the meaning of mutable.
button_mutable.place(relx = 0.5, rely =0.2, anchor = CENTER)

label_of_mutable.place(relx = 0.5, rely =0.3, anchor = CENTER)#Place the label that holds the word meaning of mutable on the root window.

button_immutable = Button(root, text = "Meaning of Immutable",command =  immutable)#Create second button to call a function to display the word meaning of immutable.
button_immutable.place(relx = 0.5, rely =0.4, anchor = CENTER)

label_of_immutable.place(relx = 0.5, rely =0.5, anchor = CENTER) #Place the label that holds the word meaning of mutable on the root window.

button_tkinter = Button(root, text = "Meaning of Tkinter", command = tkinter)# Create a third button to call a function to display the word meaning of tkinter.
button_tkinter.place(relx = 0.5, rely =0.6, anchor = CENTER)# placing it 
#Place the label that holds the word meaning of mutable on the root window.
label_of_tkinter.place(relx = 0.5, rely =0.7, anchor = CENTER)

root.mainloop()