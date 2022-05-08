
#       Hello thanks for visiting my code :D
#                   ***HAVE FUN*** 
 


from tkinter import*

LIGHT_GRAY = "#e5c083"
LABEL_COLOR = "#494949"


FONT = ("Arial", 33,'bold')
fONT=('arial', 20,'bold')

def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    

OP = Tk()
OP.iconbitmap("myIcon.ico")
OP.title("Calculator in Python") 
operator = ""
text_Input = StringVar()



#____________________________________________DISPLAY_____________________________________________


txtDisplay = Entry(OP,font=FONT, textvariable=text_Input,bg=LIGHT_GRAY,fg=LABEL_COLOR,
                 justify='right').grid(columnspan=4) 


#___________________________________________OPERATORS_____________________________________________


BtnM=Button(OP,padx=37,pady=20, bg=LIGHT_GRAY,fg=LABEL_COLOR,font=fONT,
            text="M",).grid(row=1,column="1")

btnclear=Button(OP,padx=37,pady=20,bg=LIGHT_GRAY,fg=LABEL_COLOR,font=fONT,
            text="C",command=btnClearDisplay).grid(row=1,column="0")


Btnbraket1=Button(OP,padx=43,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="(",command=lambda:btnclick("(")).grid(row=1,column="2")

Btnbracket2=Button(OP,padx=47,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text=")",command=lambda:btnclick(")")).grid(row=1,column="3")


Division=Button(OP,padx=44,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="\u00F7",command=lambda:btnclick("/")).grid(row=2,column="3")

subtraction=Button(OP,padx=47
,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR, font=fONT,
            text="-",command=lambda:btnclick("-")).grid(row=4,column="3")

Multiplication=Button(OP,padx=44,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="\u00D7",command=lambda:btnclick("*")).grid(row=3,column="3")

Dot=Button(OP,padx=43,pady=20, fg=LABEL_COLOR,bg=LIGHT_GRAY,font=fONT,
            text=".",command=lambda:btnclick(".")).grid(row=5,column="1")

Equal=Button(OP,padx=40,pady=20, fg=LABEL_COLOR,bg=LIGHT_GRAY,font=fONT,
            text="=",command=btnEqualsInput).grid(row=5,column="2")

Addition=Button(OP, padx=44,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="+",command=lambda:btnclick("+")).grid(row=5,column="3")

#____________________________________NUMBERS__________________________________________________


btn9=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="9",command=lambda:btnclick(9)).grid(row=2,column="2")

btn8=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="8",command=lambda:btnclick(8)).grid(row=2,column="1")

btn7=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="7",command=lambda:btnclick(7)).grid(row=2,column="0")

btn6=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="6",command=lambda:btnclick(6)).grid(row=3,column="0")

btn5=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="5",command=lambda:btnclick(5)).grid(row=3,column="1")

btn4=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="4",command=lambda:btnclick(4)).grid(row=3,column="2")

btn3=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="3",command=lambda:btnclick(3)).grid(row=4,column="0")

btn2=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="2",command=lambda:btnclick(2)).grid(row=4,column="1")

btn1=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="1",command=lambda:btnclick(1)).grid(row=4,column="2")

Btn0=Button(OP,padx=40,pady=20,bg=LIGHT_GRAY, fg=LABEL_COLOR,font=fONT,
            text="0",command=lambda:btnclick(0)).grid(row=5,column="0")



            

OP.mainloop()


#made by ARECZEK ;D