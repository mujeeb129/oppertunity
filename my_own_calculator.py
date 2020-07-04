from tkinter import *

window = Tk()		#Here we created a window
window.title("Calculator")			#title() - this method gives title to the window
window.geometry("300x450")			#geometry() - this method helps to give desired geometry


button_row1 = Frame(window, bg = '#000000')			#Frame - this attribute helps us to divide the window into frames(differentiating)
button_row1.pack(expand = True , fill = 'both')

button_row2 = Frame(window)
button_row2.pack(expand = True, fill = 'both')


button_row3 = Frame(window, bg = '#000000')			#Frame - this attribute helps us to divide the window into frames(differentiating)
button_row3.pack(expand = True , fill = 'both')

button_row4 = Frame(window)
button_row4.pack(expand = True, fill = 'both')

window.mainloop()
