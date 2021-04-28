from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('EMI Calculator')
root.geometry("500x400")
root.iconbitmap('loan.ico')
root.resizable(width=False, height=False)

pa = IntVar()
dp = IntVar()
ir = IntVar()
lt = IntVar()

def number():
    try:
        int(e1.get())
        int(e2.get())
        int(e3.get())
        int(e4.get())
        PAdata = pa.get()
        DPdata = dp.get()
        IRdata = ir.get()
        LTdata = lt.get()
        print("Principal Amount ", PAdata, "Down Payment ", DPdata, "Interest Rate", IRdata, "Loan Term", LTdata)
        res = calculate()
        result.config(text="The EMI is : "+str(round(res,4)))
        answer.config(text="the details are valid")
        messagebox.showinfo("details", "details accepted")
        print("The EMI is ")
        print(res)
    except ValueError:
        answer.config(text="invalid details")
    except ZeroDivisionError:
        answer.config(text = "give input other than 0")

def calculate():
    data = pa.get() - dp.get()
    Emi = emi_calculator(data, ir.get(), lt.get())
    return Emi

car = Label(root, text="CAR EMI CALCULATOR", font="times 10 bold").place(x=120, y=15)

PA = Label(root, text="Principal Amount :").place(x=30, y=40)
e1 = Entry(root,textvariable=pa)
e1.pack(padx=160, pady=40)

DP = Label(root, text="Down Payment :").place(x=30, y=100)
e2 = Entry(root,textvariable=dp)
e2.pack(padx=160, pady=0)

IR = Label(root, text="Interest Rate :").place(x=30, y=150)
e3 = Entry(root, textvariable=ir)
e3.pack(padx=160, pady=30)

LT = Label(root, text="Loan Term(in months) :").place(x=30, y=200)
e4 = Entry(root,textvariable=lt)
e4.pack(padx=160, pady=2)


my_button = Button(root, text="Calculate EMI", command=number)
my_button.pack(pady=5)

answer = Label(root, text='')
answer.pack(pady=5)

result = Label(root,text = '',fg = 'green',font=('Ariel',14))
result.pack(pady=5)

def Reset():
    pa.set("")
    dp.set("")
    ir.set("")
    lt.set("")
    answer.config(text = '')
    result.config(text = '')
    return


reset = Button(root,text="reset",command =  Reset).place(x=320,y=330)
exit = Button(root,text="exit",command = root.destroy).place(x=370,y=330)

def emi_calculator(p, r, t):
    r = r / (12 * 100)
    t = t * 12
    emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
    return emi

root.mainloop()
