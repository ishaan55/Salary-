from tkinter import *

def calc():
    cal_win = Tk()
    box = Entry(cal_win,borderwidth=3,width=50)

    def numbers(x):
        box.insert(END,x)

    def clear():
        box.delete(0,END)
        
    def add():
        global num1
        global math
        num1=float(box.get())
        math = "add"
        box.delete(0,END)

    def sub():
        global num1
        global math
        num1=float(box.get())
        math = "sub"
        box.delete(0,END)

    def mul():
        global num1
        global math
        num1=float(box.get())
        math = "mul"
        box.delete(0,END)

    def div():
        global num1
        global math
        num1=float(box.get())
        math = "div"
        box.delete(0,END)

    def equals():
        num2 = float(box.get())
        box.delete(0,END)
        
        if math=="add":
            box.insert(0,num1 + num2)

        if math=="sub":
            box.insert(0,num1 - num2)

        if math=="mul":
            box.insert(0,num1 * num2)

        if math=="div":
            box.insert(0,num1 / num2)

    button_1 = Button(cal_win,text="1",padx=30,pady=20,command=lambda: numbers("1"))
    button_2 = Button(cal_win,text="2",padx=30,pady=20,command=lambda: numbers("2"))
    button_3 = Button(cal_win,text="3",padx=30,pady=20,command=lambda: numbers("3"))
    button_4 = Button(cal_win,text="4",padx=30,pady=20,command=lambda: numbers("4"))
    button_5 = Button(cal_win,text="5",padx=30,pady=20,command=lambda: numbers("5"))
    button_6 = Button(cal_win,text="6",padx=30,pady=20,command=lambda: numbers("6"))
    button_7 = Button(cal_win,text="7",padx=30,pady=20,command=lambda: numbers("7"))
    button_8 = Button(cal_win,text="8",padx=30,pady=20,command=lambda: numbers("8"))
    button_9 = Button(cal_win,text="9",padx=30,pady=20,command=lambda: numbers("9"))
    button_0 = Button(cal_win,text="0",padx=30,pady=20,command=lambda: numbers("0"))

    button_clear = Button(cal_win,text=" C ",padx=30,pady=20,command=clear)
    button_equal = Button(cal_win,text="=",padx=30,pady=20,command=equals)
    button_add = Button(cal_win,text="+",padx=30,pady=20,command=add)
    button_sub = Button(cal_win,text="-",padx=30,pady=20,command=sub)
    button_mul = Button(cal_win,text="X",padx=30,pady=20,command=mul)
    button_div = Button(cal_win,text="/",padx=30,pady=20,command=div)

    box.grid(row=0,column=0,columnspan=4)
    button_1.grid(row=3,column=0)
    button_2.grid(row=3,column=1)
    button_3.grid(row=3,column=2)
    button_4.grid(row=2,column=0)
    button_5.grid(row=2,column=1)
    button_6.grid(row=2,column=2)
    button_7.grid(row=1,column=0)
    button_8.grid(row=1,column=1)
    button_9.grid(row=1,column=2)
    button_0.grid(row=4,column=1)
    button_clear.grid(row=4,column=0)
    button_equal.grid(row=4,column=2)
    button_add.grid(row=1,column=3)
    button_sub.grid(row=2,column=3)
    button_mul.grid(row=3,column=3)
    button_div.grid(row=4,column=3)

    cal_win.mainloop()
'''
if __name__ == '__main__':
    calc()'''

for i in range(5,0,-1):
    print(str(i)*i)