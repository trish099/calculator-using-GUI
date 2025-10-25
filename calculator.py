from tkinter import *

root = Tk()
root.geometry("334x530")
root.title("mini calculator")
root.resizable(width=False, height=False)
root.configure(bg="grey")
firstnumber = secondnumber = operatorr = None
def numbers(event):
    x = mainlabel['text']
    new = x+str(event)
    mainlabel.configure(text=new)
def clear():
    global firstnumber ,secondnumber ,operatorr
    firstnumber = None
    secondnumber = None
    operatorr = None
    mainlabel.configure(text="")
def operator(op):
    global firstnumber,secondnumber,operatorr
    firstnumber = int(mainlabel['text'])
    operatorr = op
    mainlabel.configure(text="")
def operator2():
    secondnumber = int(mainlabel['text'])
    if operatorr == "+":
        mainlabel.configure(text=str(firstnumber + secondnumber))
    if operatorr == "-":
        mainlabel.configure(text=str(firstnumber - secondnumber))
    if operatorr == "*":
        mainlabel.configure(text=str(firstnumber * secondnumber))
    if operatorr == "/":
        mainlabel.configure(text=str(firstnumber / secondnumber))
    if operatorr == "%":
        mainlabel.configure(text=str(firstnumber % secondnumber))

mainlabel = Label(root, text="",font=("Arial",35,"bold"),bg="grey")
mainlabel.grid(row=0, column=0,columnspan = 50,sticky = W ,pady = (80,20))

frame1 = Frame(root,bg="grey")
frame1.grid(row = 1, column = 0)
#row first
button7 = Button(frame1, text="7",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers(7))
button7.grid(row=1, column=0)

button8 = Button(frame1, text="8",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers(8))
button8.grid(row=1, column=1)

button9 = Button(frame1, text="9",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers(9))
button9.grid(row=1, column=2)

button_add = Button(frame1, text="+",font=("Arial",20,"bold"),relief=RIDGE,padx=21,pady=20,bg = "blue",command=lambda :operator("+"))
button_add.grid(row=1, column=3)


#row second
button4 = Button(frame1, text="4",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers("4"))
button4.grid(row=2, column=0)

button5 = Button(frame1, text="5",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers("5"))
button5.grid(row=2, column=1)

button6 = Button(frame1, text="6",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers("6"))
button6.grid(row=2, column=2)

button_sub = Button(frame1, text="-",font=("Arial",20,"bold"),relief=RIDGE,padx=25,pady=20,bg = "blue",command=lambda :operator("-"))
button_sub.grid(row=2, column=3)


#row third
button1 = Button(frame1, text="1",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers("1"))
button1.grid(row=3, column=0)

button2 = Button(frame1, text="2",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers("2"))
button2.grid(row=3, column=1)

button3 = Button(frame1, text="3",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :numbers("3"))
button3.grid(row=3, column=2)

button_mult = Button(frame1, text="*",font=("Arial",20,"bold"),relief=RIDGE,padx=24,pady=20,bg = "blue",command=lambda :operator("*"))
button_mult.grid(row=3, column=3)



#row fourth
button_clear = Button(frame1, text="C",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda:clear())
button_clear.grid(row=4, column=0)

button_equal = Button(frame1, text="=",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :operator2())
button_equal.grid(row=4, column=1)

button_div = Button(frame1, text="/",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :operator("/"))
button_div.grid(row=4, column=2)

button_per = Button(frame1, text="%",font=("Arial",20,"bold"),relief=RIDGE,padx=20,pady=20,bg = "blue",command=lambda :operator("%"))
button_per.grid(row=4, column=3)


root.mainloop()
