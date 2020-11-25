#!/usr/bin/env python3
from tkinter import *
from ascii_art import saint_clever

print(saint_clever)
window = Tk()


window.title('Unit Convertor')

def kilograms_to_grams_pounds_ounces():
  # print('converted')
  output_grams.delete(1.0, END) # clear previous output
  grams = float(input_kilograms.get()) * 1000
  output_grams.insert(END, f'{grams} grams')

  output_pounds.delete(1.0, END) # clear previous output
  pounds = float(input_kilograms.get()) * 2.20462
  output_pounds.insert(END, f'{pounds} pounds')

  output_ounces.delete(1.0, END) # clear previous output
  ounces = float(input_kilograms.get()) * 35.274
  output_ounces.insert(END, f'{ounces} ounces')

  
# label
label = Label(window, text='Unit Convertor')
label.grid(row=0, column=0)

# input window
input_kilograms = StringVar()
input_kilograms_window = Entry(window, textvariable=input_kilograms)
input_kilograms_window.grid(row=0, column=1)

# convert btn
convert_btn = Button(window, text='convert units', command=kilograms_to_grams_pounds_ounces)
convert_btn.grid(row=0, column=2)

# quit btn
quit_btn = Button(window, text='Exit Program', command=window.quit)
quit_btn.grid(row=0, column=3)

# output grams
output_grams = Text(window, height=1, width=20)
output_grams.grid(row=1, column=0)

# output pounds
output_pounds = Text(window, height=1, width=20)
output_pounds.grid(row=1, column=1)

# output ounces
output_ounces = Text(window, height=1, width=20)
output_ounces.grid(row=1, column=2)


window.mainloop()