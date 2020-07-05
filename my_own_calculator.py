from tkinter import *

window = Tk()		#Here we created a window
window.title("Calculator")			#title() - this method gives title to the window
window.geometry("270x400")			#geometry() - this method helps to give desired geometry
window.resizable(0,0)


expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	data.set(expression)

def all_clear():
	global expression
	expression = ''
	data.set(expression)

def cleared():
	global expression
	expression = expression[:-1]
	data.set(expression)















data = StringVar()

labl = Label(window, text = "Sample" , anchor = SE , height = 5 , textvariable = data , bg ='#ffffff' , fg = '#000000')
labl.pack(expand = True , fill = 'both')


button_row1 = Frame(window, bg = '#000000')			#Frame - this attribute helps us to divide the window into frames(differentiating)
button_row1.pack(expand = True , fill = 'both')

button_row2 = Frame(window)
button_row2.pack(expand = True, fill = 'both')


button_row3 = Frame(window, bg = '#000000')			#Frame - this attribute helps us to divide the window into frames(differentiating)
button_row3.pack(expand = True , fill = 'both')


button_row4 = Frame(window)
button_row4.pack(expand = True, fill = 'both')

#Buttons on row 1:
button7 = Button(
	button_row1, 
	text = '7' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 ,
	command =lambda: press(7))
button7.pack(side = LEFT, expand = True , fill = 'both')

button8 = Button(
	button_row1, 
	text = '8' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 , 
	command =lambda: press(8))
button8.pack(side = LEFT , expand = True , fill = 'both')

button9 = Button(
	button_row1, 
	text = '9' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 , 
	command =lambda: press(9))
button9.pack(side = LEFT , expand = True , fill = 'both')

buttonDEL = Button(
	button_row1, 
	text = 'DEL' , 
	font = ('Segoe UI',15) , 
	width = 1, 
	command = cleared)
buttonDEL.pack(side = LEFT , expand = True , fill = 'both')

buttonAC = Button(
	button_row1, 
	text = 'AC' , 
	font = ('Segoe UI',15) , 
	width = 1 , 
	command = all_clear)
buttonAC.pack(side = LEFT , expand = True , fill = 'both')

#Buttons on row 2:
button4 = Button(
	button_row2, 
	text = '4' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 , 
	command =lambda: press(4))
button4.pack(side = LEFT , expand = True , fill = 'both')

button5 = Button(
	button_row2, 
	text = '5' , 
	font = ('Segoe UI Bold',20) , 
	width = 1, 
	command =lambda: press(5))
button5.pack(side = LEFT , expand = True , fill = 'both')

button6 = Button(
	button_row2, 
	text = '6' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 , 
	command =lambda: press(6))
button6.pack(side = LEFT , expand = True , fill = 'both')

buttonX = Button(
	button_row2, 
	text = 'x' , 
	font = ('Segoe UI',15) , 
	width = 1 ,
	)
buttonX.pack(side = LEFT , expand = True , fill = 'both')

buttonDiv = Button(
	button_row2, 
	text = '/' , 
	font = ('Segoe UI',15) , 
	width = 1)
buttonDiv.pack(side = LEFT , expand = True , fill = 'both')

#Buttons on row 3:
button1 = Button(
	button_row3, 
	text = '1' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 ,
	command =lambda: press(1))
button1.pack(side = LEFT , expand = True , fill = 'both')

button2 = Button(
	button_row3, 
	text = '2' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 , 
	command =lambda: press(2))
button2.pack(side = LEFT , expand = True , fill = 'both')

button3 = Button(
	button_row3, 
	text = '3' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 ,
	command =lambda: press(3))
button3.pack(side = LEFT , expand = True , fill = 'both')

buttonPlus = Button(
	button_row3, 
	text = '+' , 
	font = ('Segoe UI',15) , 
	width = 1)
buttonPlus.pack(side = LEFT , expand = True , fill = 'both')

buttonSub = Button(
	button_row3, 
	text = '-' , 
	font = ('Segoe UI',15) , 
	width = 1)
buttonSub.pack(side = LEFT , expand = True , fill = 'both')

#Buttons on row 4 :
button0 = Button(
	button_row4, 
	text = '0' , 
	font = ('Segoe UI Bold',20) , 
	width = 1 , 
	command =lambda: press(0))
button0.pack(side = LEFT , expand = True , fill = 'both')

buttonDot = Button(
	button_row4, 
	text = '.' , 
	font = ('Segoe UI',15) , 
	width = 1)
buttonDot.pack(side = LEFT , expand = True , fill = 'both')

buttonPower = Button(
	button_row4, 
	text = '^' , 
	font = ('Segoe UI',15) , 
	width = 1)
buttonPower.pack(side = LEFT , expand = True , fill = 'both')

buttonEqual = Button(
	button_row4, 
	text = '=' , 
	font = ('Segoe UI',15) , 
	width = 4)
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
