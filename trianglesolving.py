from tkinter import *
from tkinter import ttk
def validate():
    if leg1.get() == '' and leg2.get().replace('.', '', 1).isnumeric() and hypotenuse.get().replace('.', '', 1).isnumeric():
        if float(leg2.get()) >= float(hypotenuse.get()):
            status.set("Invalid right Triangle")
            return False
        if float(leg2.get()) == 0 or float(hypotenuse.get()) == 0:
            status.set("Invalid side length")
            return False
        status.set("Valid right Triange")
        return True
    if leg2.get() == '' and leg1.get().replace('.', '', 1).isnumeric() and hypotenuse.get().replace('.', '', 1).isnumeric():
        if float(leg1.get()) >= float(hypotenuse.get()):
            status.set("Invalid right Triangle")
            return False
        if float(leg1.get()) == 0 or float(hypotenuse.get()) == 0:
            status.set("Invalid side length")
            return False
        status.set("Valid right Triange")
        return True
    if hypotenuse.get() == '' and leg1.get().replace('.', '', 1).isnumeric() and leg2.get().replace('.', '', 1).isnumeric():
        if float(leg1.get()) == 0 or float(leg2.get()) == 0:
            status.set("Invalid side length")
            return False
        status.set("Valid right Triange")
        return True
    status.set("Not enough info/already filled/ invalid side lengths")
def calculate(*args):
    canvas.delete("all")
    if validate():
        if hypotenuse.get() == '':
            hypotenuse.set(pow(pow(float(leg1.get()), 2) + pow(float(leg2.get()), 2), 0.5))
        elif leg1.get() == '':
            leg1.set(pow(pow(float(hypotenuse.get()), 2) - pow(float(leg2.get()), 2), 0.5))
        elif leg2.get() == '':
            leg2.set(pow(pow(float(hypotenuse.get()), 2) - pow(float(leg1.get()), 2), 0.5))
        draw(float(leg1.get()), float(hypotenuse.get()), float(leg2.get()))

def draw(a, b, c):
    # determine corner points of triangle with sides a, b, c
    if a >= b:
        temp = b
        b = a
        a = temp
    A = (0, 0)
    B = (c, 0)
    hc = (2 * (a**2*b**2 + b**2*c**2 + c**2*a**2) - (a**4 + b**4 + c**4))**0.5 / (2.*c)
    dx = (b**2 - hc**2)**0.5
    if abs((c - dx)**2 + hc**2 - a**2) > 0.01: dx = -dx # dx has two solutions
    C = (dx, hc)

    # move away from topleft, scale up a bit, convert to int
    coords = [(x + 1) * 10 for x in A+B+C]
    canvas.create_polygon(*coords, fill='white', outline = 'black')
root = Tk()
root.title("Right triangle solver and visualizer")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
leg1 = StringVar()
leg2 = StringVar()
hypotenuse = StringVar()
status = StringVar()
ttk.Label(mainframe, text="leg1").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="leg2").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text= "hypotenuse").grid(column=1, row=3, sticky=W)
ttk.Entry(mainframe, textvariable=leg1).grid(column=2, row=1, sticky=W)
ttk.Entry(mainframe, textvariable=leg2).grid(column=2, row=2, sticky=E)
ttk.Entry(mainframe, textvariable= hypotenuse).grid(column=2, row=3, sticky=E)
ttk.Label(mainframe, text= 'Status:').grid(column=2, row=4, sticky=E)
ttk.Label(mainframe, textvariable=status).grid(column=3, row=4, sticky=S)
canvas = Canvas(root, width=300, height= 200)
canvas.grid(column=0, row=6, sticky='W', rowspan= 6, columnspan=2, pady=10)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", calculate)

root.mainloop()
