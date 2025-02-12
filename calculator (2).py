
from tkinter import *

root = Tk()
root.title("Calculator")
root["bg"]="lightgreen"
width = 400
height = 255

sys_width = root.winfo_screenwidth()
sys_height = root.winfo_screenheight()
c_x = int(sys_width/2 - width/2)
c_y = int(sys_height/2 - height/2)
root.geometry(f"{width}x{height}+{c_x}+{c_y}")
root.resizable(False,False)



operator = ''

def buttonclick(numbers):
    global operator
    operator = operator+numbers
    calculatorfield.delete(0,END)
    calculatorfield.insert(END, operator)

def clear():
    global operator
    operator=''
    calculatorfield.delete(0,END)

def answer():
    global operator
    result = str(eval(operator))
    calculatorfield.delete(0,END)
    calculatorfield.insert(0, result)
    operator=''
calculatorfield = Entry(root, width = 40)
calculatorfield.grid(row=0, column=0, columnspan=4)


button1 = Button(root, text = '1',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('1'), height = 2,width = 7)
button1.grid(row=1, column=0)
button2 = Button(root, text = '2',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('2'), height = 2,width = 7)
button2.grid(row=1, column=1)
button3 = Button(root, text = '3',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('3'), height = 2,width = 7)
button3.grid(row=1, column=2)
button4 = Button(root, text = '4',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('4'), height = 2,width = 7)
button4.grid(row=2, column=0)
button5 = Button(root, text = '5',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('5'), height = 2,width = 7)
button5.grid(row=2, column=1)
button6 = Button(root, text = '6',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('6'), height = 2,width = 7)
button6.grid(row=2, column=2)
button7 = Button(root, text = '7',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('7'), height = 2,width = 7)
button7.grid(row=3, column=0)
button8 = Button(root, text = '8',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('8'), height = 2,width = 7)
button8.grid(row=3, column=1)
button9 = Button(root, text = '9',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('9'), height = 2,width = 7)
button9.grid(row=3, column=2)
button0 = Button(root, text = '0',padx=10,bd=10,bg="light blue",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('0'), height = 2,width = 7)
button0.grid(row=4, column=1)
button_add = Button(root, text = '+',padx=10,bd=10,bg="yellow",fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('+'), height = 2,width = 7)
button_add.grid(row=1, column=3)
button_subr = Button(root, text = '-',padx=10,bd=10,fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('-'), height = 2,width = 7)
button_subr.grid(row=2, column=3)
button_multi = Button(root, text = 'x',padx=10,bd=10,fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('*'), height = 2,width = 7)
button_multi.grid(row=3, column=3)
button_divide = Button(root, text = '/',padx=10,bd=10,fg="black",font=("arial",10,"bold"),command=lambda:buttonclick('/'), height = 2,width = 7)
button_divide.grid(row=4, column=3)
button_ans = Button(root, text = '=',padx=10,bd=10,fg="black",font=("arial",10,"bold"),command=answer, height = 2,width = 7)
button_ans.grid(row=4, column=0)
button_clear = Button(root, text = 'clear',padx=10,bd=10,bg="Red",fg="black",font=("arial",10,"bold"),command=clear, height = 2,width = 7)
button_clear.grid(row=4, column=2)
root.mainloop()