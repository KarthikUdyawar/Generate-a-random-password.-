# import
from tkinter import *
import random, string
import pyperclip

# function to generate password
def Generator():
    password = ''
    
    for y in range(pass_len.get()):
        if (ch.get() == 1):                 #* Only numbers
            password = password + random.choice(string.digits)
        elif (ch.get() == 2):               #* Lower-case letters
            password = password + random.choice(string.ascii_lowercase)
        elif (ch.get() == 3):               #* Upper-case letters
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase)
        elif (ch.get() == 4):               #* Alphanumeric
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        else:                               #* Every Keyword symbol
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
    
# function to copy password
def Copy_password():
    pyperclip.copy(pass_str.get())

# main 
if __name__ == '__main__':
    # initialization
    root = Tk()
    root.geometry("400x400")
    root.resizable(0,0)
    root.title("PASSWORD GENERATOR")
    
    # variables
    pass_len = IntVar()
    ch = IntVar()
    pass_str = StringVar()
    
    Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()         #* header
    
    # Spinbox for length of password
    pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
    length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 15, state="readonly").pack()
    
    # Radio Button for type of password
    r1 = Radiobutton(root, text="Only numbers", value=1, variable=ch).pack()
    r2 = Radiobutton(root, text="Lower-case letters", value=2, variable=ch).pack()
    r3 = Radiobutton(root, text="Upper-case letters", value=3, variable=ch).pack()
    r4 = Radiobutton(root, text="Alphanumeric", value=4, variable=ch).pack()
    r5 = Radiobutton(root, text="Every Keyword symbol", value=5, variable=ch).pack()
    
    Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)   #* submit button
    
    Entry(root , textvariable = pass_str, width = 40, state="readonly").pack()      #* Output 
    
    Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)  #* button to copy 

    root.mainloop()                                                                 #* mainloop
