'''
things to do :
	1. Create the frontend(purely for confidence)
	2. Backend work : -create a global variable for user input through button
					  -store the expression in an string variable
					  -press() : to concatinate with global variable to make an expression
					  -all_clear() : to clear all the characters in the string variable
					  -clear() : Delete last entered character
'''
from tkinter import *

window = Tk()		#Here we created a window
window.title("Calculator")			#title() - this method gives title to the window
window.geometry("270x400+100+100")			#geometry() - this method helps to give desired geometry
window.resizable(0,0)

#a variable is created out side the funtions to make it global
expression = ""

#funtions or commands for button
def press(num):
	global expression
	expression = expression + str(num)
	data.set(expression)

def all_clear():
	global expression
	expression = ''
	data.set(expression)

def clear():
	global expression
	expression = expression[:-1]
	data.set(expression)

def equal_to():
	global expression
	if '/0' in expression :
		expression = ''
		data.set('ERROR')
	if expression[0] == '0':
		expression = expression[1:]
	expression = str(eval(expression))
	data.set(expression)


data = StringVar()


menu_bar = Menu(window , activeborderwidth = 0 , bd = 0 , bg = '#ffffff' ,)
file_menu = Menu(menu_bar , tearoff = 0 , activeborderwidth = 0 , relief = GROOVE)
menu_bar.add_command(label = "STANDARD" , font = ('Segoe UI Bold' , 14) , command = None ,)

window.config(menu = menu_bar)


labl = Label(
	window,
	text = "Sample" ,
	anchor = SE ,
	textvariable = data ,
	font = ('Segoe UI Bold' , 22) ,
	height = 3 ,
	bg ='#ffffff' ,
	fg = '#000000')
labl.pack(expand = True , fill = 'both')



button_row1 = Frame(window)			#Frame - this attribute helps us to divide the window into frames(differentiating)
button_row1.pack(expand = True , fill = 'both')

button_row2 = Frame(window)
button_row2.pack(expand = True, fill = 'both')


button_row3 = Frame(window)			#Frame - this attribute helps us to divide the window into frames(differentiating)
button_row3.pack(expand = True , fill = 'both')


button_row4 = Frame(window)
button_row4.pack(expand = True, fill = 'both')

#Buttons on row 1:
button7 = Button(
	button_row1,
	text = '7' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(7))
button7.pack(side = LEFT, expand = True , fill = 'both')

button8 = Button(
	button_row1,
	text = '8' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(8))
button8.pack(side = LEFT , expand = True , fill = 'both')

button9 = Button(
	button_row1,
	text = '9' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(9))
button9.pack(side = LEFT , expand = True , fill = 'both')

buttonDEL = Button(
	button_row1,
	text = 'DEL' ,
	font = ('Segoe UI',15) ,
	width = 1,
	bd = 0 ,
	relief = GROOVE ,
	activebackground = '#F23C34' ,
	activeforeground = '#ffffff' ,
	highlightbackground = '#ffffff' ,
	highlightcolor = '#F23C34' ,
	fg = '#F23C34' ,
	command = clear)
buttonDEL.pack(side = LEFT , expand = True , fill = 'both')

buttonAC = Button(
	button_row1,
	text = 'AC' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = all_clear)
buttonAC.pack(side = LEFT , expand = True , fill = 'both')

#Buttons on row 2:
button4 = Button(
	button_row2,
	text = '4' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(4))
button4.pack(side = LEFT , expand = True , fill = 'both')

button5 = Button(
	button_row2,
	text = '5' ,
	font = ('Segoe UI Bold',20) ,
	width = 1,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(5))
button5.pack(side = LEFT , expand = True , fill = 'both')

button6 = Button(
	button_row2,
	text = '6' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(6))
button6.pack(side = LEFT , expand = True , fill = 'both')

buttonX = Button(
	button_row2,
	text = '*' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda : press('*'))
buttonX.pack(side = LEFT , expand = True , fill = 'both')

buttonDiv = Button(
	button_row2,
	text = '/' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press('/'))
buttonDiv.pack(side = LEFT , expand = True , fill = 'both')

#Buttons on row 3:
button1 = Button(
	button_row3,
	text = '1' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(1))
button1.pack(side = LEFT , expand = True , fill = 'both')

button2 = Button(
	button_row3,
	text = '2' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(2))
button2.pack(side = LEFT , expand = True , fill = 'both')

button3 = Button(
	button_row3,
	text = '3' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(3))
button3.pack(side = LEFT , expand = True , fill = 'both')

buttonPlus = Button(
	button_row3,
	text = '+' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = RIDGE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press('+'))
buttonPlus.pack(side = LEFT , expand = True , fill = 'both')

buttonSub = Button(
	button_row3,
	text = '-' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	highlightbackground = '#ffffff' ,
	bd = 0 ,
	relief = GROOVE ,
	command = lambda : press('-'))
buttonSub.pack(side = LEFT , expand = True , fill = 'both')

#Buttons on row 4 :
button0 = Button(
	button_row4,
	text = '0' ,
	font = ('Segoe UI Bold',17) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda: press(0))
button0.pack(side = LEFT , expand = True , fill = 'both')

buttonDot = Button(
	button_row4,
	text = '.' ,
	font = ('Segoe UI',17) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press('.'))
buttonDot.pack(side = LEFT , expand = True , fill = 'both')

buttonPower = Button(
	button_row4,
	text = '^' ,
	font = ('Segoe UI',17) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press('**'))
buttonPower.pack(side = LEFT , expand = True , fill = 'both')

buttonEqual = Button(
	button_row4,
	text = '=' ,
	font = ('Segoe UI',17) ,
	width = '5' ,
	bd = 0 ,
	relief = GROOVE ,
	bg = '#FFE138' ,
	highlightbackground = '#FFFFFF' ,
	command = equal_to)
buttonEqual.pack(side = LEFT , expand = True , fill = 'both')
'''
button7 = Button(
	button_row4,
	text = '7' ,
	font = ('Segoe UI Bold',20) ,
	width = 1)
button7.pack(side = LEFT , expand = True , fill = 'both')
'''


window.mainloop()
