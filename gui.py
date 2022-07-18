from tkinter import *
from tkinter import ttk
from tax_credit import *
from strings import *
from constants import *

window = Tk()
window.title(title)
window.geometry(str(sizeX) + "x" + str(sizeY))
windowFrame = ttk.Frame(window)
entry = ttk.Entry(windowFrame, width=theWidth)
entry.insert(0, entryHint)
labels = []


def destroyEveryLabelAndClear():
    for l in labels:
        l.destroy()
    labels.clear()


def registerLabel(label):
    labels.append(label)
    label.grid(column=0, row=2)


def onOkButtonClick():
    destroyEveryLabelAndClear()
    x = tax_credit(float(entry.get()))
    label = ttk.Label(window, text=labelTxt + str(x))
    registerLabel(label)


okButton = ttk.Button(windowFrame, width=theWidth, text=buttonTxt,
                      command=onOkButtonClick)


def drawGUI():
    windowFrame.grid()
    entry.grid(column=0, row=1)
    okButton.grid()
    window.mainloop()