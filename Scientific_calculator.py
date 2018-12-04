from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()    # name of the app
root.title("Alex Scientific Calculator")  # title of app
root.configure(background="powder blue")   # bc of the app
root.resizable(width=FALSE, height=FALSE)  # fix size of app
root.geometry("480x568+0+0")    # size of the app

calc = Frame(root)     # Frame of app
calc.grid()            # position of frame

# ================Calculator Class==========================================================================
class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False


    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)


    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)


    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)



added_value = Calc()



# ================Widgets=================================================================================
# ================Text Display============================================================================
txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)    # display text
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")      # initial display text

# ================Buttons=================================================================================
# ================Main Numbers============================================================================
numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text= numberpad[i]))
        btn[i].grid(row=j, column=k, pady =1)
        # Call the added function
        btn[i]["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
        i += 1
# ================Clear Buttons==========================================================================
btnClear = Button(calc, text= chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                  command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)    # Top Button C  clear

btnAllClear = Button(calc, text= chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                     command=added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)    # Top Button CE  clear

btnSq = Button(calc, text= "√", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
               command=added_value.squared).grid(row=1, column=2, pady=1)    # Top Button C  clear

btnAdd = Button(calc, text= "+", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                command = lambda : added_value.operation("add")).grid(row=1, column=3, pady=1)    # Top Button CE  clear

btnSub = Button(calc, text= "-", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                command = lambda : added_value.operation("sub")).grid(row=2, column=3, pady=1)    # Top Button CE  clear

btnMult = Button(calc, text= "*", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                 command = lambda : added_value.operation("multi")).grid(row=3, column=3, pady=1)    # Top Button CE  clear

btnDiv = Button(calc, text= chr(247), width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                command = lambda : added_value.operation("divide")).grid(row=4, column=3, pady=1)    # Top Button CE  clear

btnZero = Button(calc, text= "0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg="powder blue", command = lambda : added_value.numberEnter(0)).grid(row=5, column=0, pady=1)    # Top Button CE  clear

btnDot = Button(calc, text= ".", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                command = lambda : added_value.numberEnter(".")).grid(row=5, column=1, pady=1)    # Top Button CE  clear

btnPM = Button(calc, text= chr(177), width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
               command=added_value.mathsPM).grid(row=5, column=2, pady=1)    # Top Button CE  clear

btnEqual = Button(calc, text= "=", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                  command=added_value.sum_of_total).grid(row=5, column=3, pady=1)    # Top Button CE  clear

# ================Scientific Calculator==========================================================================
btnPi = Button(calc, text= "Π", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
               command = added_value.pi).grid(row=1, column=4, pady=1)    # Top Button C  clear

btnCos = Button(calc, text= "cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                command=added_value.cos).grid(row=1, column=5, pady=1)    # Top Button CE  clear

btntan = Button(calc, text= "tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                command=added_value.tan).grid(row=1, column=6, pady=1)    # Top Button C  clear

btnsin = Button(calc, text= "sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                command=added_value.sin).grid(row=1, column=7, pady=1)    # Top Button CE  clear

# ===============================================================================================================

btn2Pi = Button(calc, text= "2Π", width=6, height=2, font=('arial', 20, 'bold'),bd=4,bg="powder blue",
                command=added_value.tau).grid(row=2, column=4, pady=1)    # Top Button CE  clear

btnCosh = Button(calc, text= "cosh", width=6, height=2, font=('arial', 20, 'bold'),bd=4,
                 command=added_value.cosh).grid(row=2, column=5, pady=1)    # Top Button CE  clear

btntanh = Button(calc, text= "tanh", width=6, height=2, font=('arial', 20, 'bold'),bd=4,
                 command=added_value.tanh).grid(row=2, column=6, pady=1)    # Top Button CE  clear

btnsinh = Button(calc, text= "sinh", width=6, height=2, font=('arial', 20, 'bold'),bd=4,
                 command=added_value.sinh).grid(row=2, column=7, pady=1)    # Top Button CE  clear

# ===============================================================================================================

btnlog = Button(calc, text= "log", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                command=added_value.log).grid(row=3, column=4, pady=1)    # Top Button CE  clear

btnExp = Button(calc, text= "Exp", width=6, height=2, font=('arial', 20, 'bold'),bd=4,
                command=added_value.exp).grid(row=3, column=5, pady=1)    # Top Button CE  clear

btnMod = Button(calc, text= "Mod", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                command = lambda : added_value.operation("mod")).grid(row=3, column=6, pady=1)    # Top Button CE  clear

btnE = Button(calc, text= "e", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
              command=added_value.e).grid(row=3, column=7, pady=1)    # Top Button CE  clear

# ===============================================================================================================

btnlog2 = Button(calc, text= "log2", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                 command=added_value.log2).grid(row=4, column=4, pady=1)    # Top Button CE  clear

btndeg = Button(calc, text= "deg", width=6, height=2, font=('arial', 20, 'bold'),bd=4,
                command=added_value.degrees).grid(row=4, column=5, pady=1)    # Top Button CE  clear

btnacosh = Button(calc, text= "acosh", width=6, height=2, font=('arial', 20, 'bold'),bd=4,
                  command=added_value.acosh).grid(row=4, column=6, pady=1)    # Top Button CE  clear

btnasinh = Button(calc, text= "asinh", width=6, height=2, font=('arial', 20, 'bold'),bd=4,
                  command=added_value.asinh).grid(row=4, column=7, pady=1)    # Top Button CE  clear

# ===============================================================================================================

btnlog10 = Button(calc, text= "log10", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                  command=added_value.log10).grid(row=5, column=4, pady=1)    # Top Button CE  clear

btnlog1p = Button(calc, text= "log1p", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                  command=added_value.log1p).grid(row=5, column=5, pady=1)    # Top Button CE  clear

btnexpm1 = Button(calc, text= "expm1", width=6, height=2, font=('arial', 20, 'bold'),bd=4,bg="powder blue",
                  command=added_value.expm1).grid(row=5, column=6, pady=1)    # Top Button CE  clear

btnlgamma = Button(calc, text= "lgamma", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue",
                   command=added_value.lgamma).grid(row=5, column=7, pady=1)    # Top Button CE  clear


lblDisplay = Label(calc, text="Alex\n Scientific Calculator", font=('arial', 30, 'bold'), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)
# ================End of Scientific =================================================================================

# ================Functions=================================================================================
def Standard():
    root.resizable(width=FALSE, height=FALSE)  # fix size of app
    root.geometry("480x568+0+0")  # size of the standard calculator

def Scientific():
    root.resizable(width=FALSE, height=FALSE)  # fix size of app
    root.geometry("944x568+0+0")  # size of the scientific calculator

def iExit():                            # title of message box & message
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return        # exit function

# ================Menu=================================================================================
menubar = Menu(calc)   # Menubar inside the cal frame
# ================File Menu=================================================================================
filemenu = Menu(menubar, tearoff=0)   # file menu inside menubar
menubar.add_cascade(label="File", menu=filemenu)  # menu name
filemenu.add_command(label = "Standard", command = Standard)     # menu leabel 1
filemenu.add_separator()     # add separetor between them
filemenu.add_command(label = "Scientific", command = Scientific)     # menu leabel 2
filemenu.add_separator()     # add separetor between them
filemenu.add_command(label = "Exit", command = iExit)     # menu leabel 3

# ================Edit Menu=================================================================================
editmenu = Menu(menubar, tearoff=0)   # Edit menu inside menubar
menubar.add_cascade(label="Edit", menu=editmenu)   # menu name
editmenu.add_command(label = "Cut")     # menu leabel 1
editmenu.add_separator()     # add separetor between them
editmenu.add_command(label = "Copy")     # menu leabel 2
editmenu.add_separator()     # add separetor between them
editmenu.add_command(label = "Paste")     # menu leabel 3

# ================Help Menu=================================================================================
helpmenu = Menu(menubar, tearoff=0)   # Edit menu inside menubar
menubar.add_cascade(label="Help", menu=helpmenu)   # menu name
helpmenu.add_command(label = "View Help")     # menu leabel 1



# ================Run Program=================================================================================
root.configure(menu=menubar)  # custom system display
root.mainloop()               # starts the program


# program by
# Alexander bediako alexbedgh@yahoo.com
# Beijing