#------------------------------------
#probibilit simulator
#Made by Lincoln Jones/BlackHatGorilla
#v0.1.03
#made with tkinter
#------------------------------------
import tkinter as tk
import random

root = tk.Tk()

root.title("Probibilty Simulatorv0.0.1")
root.geometry("800x300")

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))

TITLE_FONT = ("Comic Sans MS", 40, "bold")
SUBTITLE_FONT = ("Comic Sans MS", 30)
FONT = ("Comic Sans MS", 20)


# folowing function from stack overflow
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def startCalculation():
    global nFlips
    global nHeads
    global nTails
    nHeads = 0
    nTails = 0
    i = 0
    while i < nFlips.get():
        flip = random.randint(0, 1)
        if flip == 0:
            nHeads = nHeads + 1
            i = i + 1
        if flip == 1:
            nTails = nTails + 1
            i = i + 1

def showResultWindow():
    flips = nFlips.get()
    
    percentOHeads = (nHeads / flips) * 100 
    percentOTails = (nTails / flips) * 100

    top = tk.Toplevel()
    top.title("results")
    top.geometry('280x280')
    dHeads = tk.Label(top, text = 'Number of heads = ' + str(nHeads))
    dTails = tk.Label(top, text = 'Number of tails = ' + str(nTails))
    dTailsPercent = tk.Label(top, text = '%Tails = %' + str(percentOTails))
    dHeadsPercent = tk.Label(top, text = '%Heads = %' + str(percentOHeads))

    dHeads.configure(font = FONT)
    dTails.configure(font = FONT)
    dHeads.grid(row = 1, column = 1)
    dTails.grid(row = 2, column = 1)
    dHeadsPercent.configure(font = FONT)
    dTailsPercent.configure(font = FONT)
    dHeadsPercent.grid(row = 4, column = 1)
    dTailsPercent.grid(row = 5, column = 1)

title = tk.Label(text = "PROBIBILTY SIMULATOR v0.0.1")
title.configure(font = TITLE_FONT)
title.grid(row = 5, column = 2)



global nFlips


textN1 = tk.Label(root, text = "Choose number of times to flip coin") 
textN1.configure(font = SUBTITLE_FONT)
textN1.grid(row = 6, column = 2)

nFlips = tk.Scale(root, from_ = 1, to = 500, orient = "horizontal")
nFlips.grid(row = 8, column = 2)
nFlips.configure(length = 500)

startButton = tk.Button(root, text = "start calulating", command = combine_funcs(startCalculation, showResultWindow))
startButton.grid(row = 9, column = 2)

root.mainloop()