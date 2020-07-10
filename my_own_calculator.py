#!/usr/bin/env python3
from tkinter import *
import math		#math module is used to import advanced math functions
'''
things to do :
	1. Create the frontend(purely for confidence)
	2. Backend work : -create a global variable for user input through button
					  -store the expression in an string variable
					  -press() : to concatinate with global variable to make an expression
					  -all_clear() : to clear all the characters in the string variable
					  -clear() : Delete last entered character
'''

window = Tk()		#Here we created a window
window.title("Calculator")			#title() - this method gives title to the window
window.geometry("270x400+100+100")			#geometry() - this method helps to give desired geometry
window.resizable(0,0)		#resizable() - this method enables us to resize the window((1,1) for changing height and width)
window.config(bg = '#ffffff')		#config() - this is to configure the whole widget
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
#This condition check wheather the given expression is valid or not
	if '/0' in expression:
		expression = ''
		data.set('ERROR')
#This iteration removes 0s from the starting of the expression(doesn't remove 0s after the operator)
	for i in range(0,int(len(expression))):
		if expression[0] == '0':
			expression = expression[1:]
		else:
			expression = str(eval(expression))
			data.set(expression)
			break

def fsin():
	global expression
	expression = str(math.sin(float(expression)))
	data.set(expression)

def fcos():
	global expression
	expression = str(math.cos(float(expression)))
	data.set(expression)

def ftan():
	global expression
	expression = str(math.tan(float(expression)))
	data.set(expression)

def flog():
	global expression
	expression = str(math.log(float(expression)))
	data.set(expression)

def fact():
	global expression
	if expression[0] == '-':
		expression = ''
		data.set('ERROR')
	else :
		expression = str(math.factorial(int(expression)))
		data.set(expression)

def fexp():
	global expression
	expression = str(math.exp(int(expression)))
	data.set(expression)

#This function is used switch from BASIC to ADVANCED
def clicked():
	if switch.config('text')[-1] == 'BASIC' :
		switch.config(text='ADVANCED' )
		window.geometry('570x400')
		advanced()

	else :
		switch.config(text = 'BASIC')
		window.geometry('270x400')
		hiding()


#This function is used to create buttons for advanced mode
def advanced():
	button0.config(font = ('Segoe UI Bold',20))
	buttonPower.config(font = ('Segoe UI',15))
	buttonDot.config(font = ('Segoe UI',15))
	buttonEqual.config(width = 1)
	'''
	buttonEqual.config(width = 1 ,
		font = ('Segoe UI' , 15) ,
		text = '.' ,
		bd = 0 ,
		bg = '#D9D9D9' ,
		relief = GROOVE ,
		highlightbackground = '#ffffff' ,
		command = lambda : press('.'))
	buttonDot.config(
		text = '=' ,
		font = ('Segoe UI',15) ,
		width = '1' ,
		bd = 0 ,
		relief = GROOVE ,
		bg = '#FFE138' ,
		highlightbackground = '#FFFFFF' ,
		command = equal_to)
		'''
	button_sin.pack(expand = True , side = RIGHT , fill = 'both')
	button_cos.pack(expand = True , side = RIGHT , fill = 'both')
	button_tan.pack(expand = True , side = LEFT , fill = 'both')
	button_log.pack(expand = True , side = LEFT , fill = 'both')
	button_exp.pack(expand = True , side = LEFT , fill = 'both')
	button_pi.pack(expand = True , side = LEFT , fill = 'both')
	buttonOB.pack(expand = True , side = LEFT , fill = 'both')
	buttonCB.pack(expand = True , side = LEFT , fill = 'both')
	buttonPower.pack(side = RIGHT)
	buttonEqual.pack(side = RIGHT)
	buttonDot.pack(side = RIGHT)
	button_fact.pack(expand = True , side = LEFT , fill = 'both')

def hiding():
	button_sin.forget()
	button_cos.forget()
	button_tan.forget()
	button_log.forget()
	button_exp.forget()
	button_pi.forget()
	buttonOB.forget()
	buttonCB.forget()
	button_fact.forget()
	buttonEqual.config(width = 5)
	button0.config(font = ('Segoe UI Bold',17))
	buttonPower.config(font = ('Segoe UI',17))
	buttonDot.config(font = ('Segoe UI',17))
	#buttonDot.config(width = 1 ,
	#	font = ('Segoe UI' , 17) ,
	#	text = '.' ,
	#	bd = 0 ,
	#	bg = '#D9D9D9' ,
	#	relief = GROOVE ,
	#	highlightbackground = '#ffffff' ,
	#	command = lambda : press('.'))
	#buttonEqual.config(
	#	text = '=' ,
	#	font = ('Segoe UI',17) ,
	#	width = '5' ,
	#	bd = 0 ,
	#	relief = GROOVE ,
	#	bg = '#FFE138' ,
	#	highlightbackground = '#FFFFFF' ,
	#	command = equal_to)
	buttonEqual.pack(side = RIGHT)
	buttonPower.pack(side = LEFT)
	buttonDot.pack(side = LEFT)


def day_night():
	if night_mode.config('text')[-1]=='D':
		night_mode.config(text = 'N')
		nighty()
	else:
		night_mode.config(text = 'D')




def nighty():
	switch.config(bg = '#152642' , fg = '#83A9E5' , highlightbackground = '#152642')
	labl.config(bg = '#152642' , fg = '#83A9E5')
	button_row.config(bg = '#152642')
	button0.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button1.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button2.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button3.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button4.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button5.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button6.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button7.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button8.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button9.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonPlus.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonOB.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonCB.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonDiv.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonSub.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonPower.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button_pi.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button_exp.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonDot.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonX.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button_sin.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button_cos.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button_tan.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button_log.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	button_fact.config(
		bg = '#081B33' ,
		fg = '#83A9E5' ,
		activebackground = '#83A9E5' ,
		activeforeground = '#081B33' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')
	buttonDEL.config(
		bg = '#602080' ,
		fg = '#b030b0' ,
		activebackground = '#b030b0' ,
		activeforeground = '#602080' ,
		highlightbackground = '#152642' ,
		highlightcolor = '#83A9E5')


def day():
	window.config(bg = '#ffffff')


data = StringVar()

button_row = Frame(window , height = 0 , bg = '#ffffff')
button_row.pack(expand = True , side = TOP , fill = 'both')

global switch
switch = Button(
	button_row ,
	text= "BASIC" ,
	font= ('Verdana', 10) ,
	bg = '#ffffff' ,
	activebackground = '#ffffff' ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	width = 7 ,
	bd = 0 ,
	command = clicked)
switch.pack(side = LEFT , fill = 'both')

global night_mode
night_mode = Button(
	button_row ,
	text = 'D' ,
	bg = '#000000' ,
	fg = '#ffffff' ,
	width = 1 ,
	command = day_night)
night_mode.pack(side = RIGHT , padx = 7)

#This attribute Label() helps you create screen for displaying characters
labl = Label(
	window,
	text = "Sample" ,
	anchor = SE ,
	textvariable = data ,
	font = ('Segoe UI Bold' , 22) ,
	height = 2 ,
	bg ='#ffffff' ,
	fg = '#000000')
labl.pack(expand = True , fill = 'both')


#Frame attribute acts as div for master window
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

button_sin = Button(
	button_row1 ,
	text = 'sin' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = fsin)
#button_sin.pack(expand = True , side = RIGHT , fill = 'both')

button_cos = Button(
	button_row1 ,
	text = 'cos' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = fcos)
#button_cos.pack(expand = True , side = RIGHT , fill = 'both')

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
buttonDEL.pack(side = RIGHT , expand = True , fill = 'both')

buttonAC = Button(
	button_row1,
	text = 'AC' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	activebackground = '#F23C34' ,
	activeforeground = '#ffffff' ,
	bg = '#F23C34' ,
	fg = '#ffffff' ,
	highlightbackground = '#ffffff' ,
	command = all_clear)
buttonAC.pack(side = RIGHT , expand = True , fill = 'both')

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

button_tan = Button(
	button_row2 ,
	text = 'tan' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff',
	command = ftan )
#button_tan.pack(expand = True , side = RIGHT , fill = 'both')

button_log = Button(
	button_row2 ,
	text = 'log' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = flog)
#button_log.pack(expand = True , side = RIGHT , fill = 'both')

buttonX = Button(
	button_row2,
	text = '*' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda : press('*'))
buttonX.pack(side = RIGHT , expand = True , fill = 'both')

buttonDiv = Button(
	button_row2,
	text = '/' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press('/'))
buttonDiv.pack(side = RIGHT , expand = True , fill = 'both')

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

button_pi = Button(
	button_row3,
	text = 'pi' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command =lambda : press(str(math.pi)))

button_exp = Button(
	button_row3,
	text = 'e^' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press(str(math.e) + '**'))

buttonPlus = Button(
	button_row3,
	text = '+' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = RIDGE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press('+'))
buttonPlus.pack(side = RIGHT , expand = True , fill = 'both')

buttonSub = Button(
	button_row3,
	text = '-' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	highlightbackground = '#ffffff' ,
	bd = 0 ,
	relief = GROOVE ,
	command = lambda : press('-'))
buttonSub.pack(side = RIGHT , expand = True , fill = 'both')

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

buttonOB = Button(
	button_row4,
	text = '(' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press('('))

buttonCB = Button(
	button_row4,
	text = ')' ,
	font = ('Segoe UI Bold',20) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = lambda : press(')'))

button_fact = Button(
	button_row4,
	text = '!' ,
	font = ('Segoe UI',15) ,
	width = 1 ,
	bd = 0 ,
	relief = GROOVE ,
	highlightbackground = '#ffffff' ,
	command = fact)

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


window.mainloop()
