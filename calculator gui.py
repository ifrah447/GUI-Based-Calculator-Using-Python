
from tkinter import *
def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def btncleardisplay():
    global operator
    operator=""
    text_Input.set("")
def btnequalInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
cal=Tk()
cal.title("calculator")
operator=""
text_Input=StringVar()
txtdisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)

b7=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',command=lambda :btnclick(7)).grid(row=1,column=0)
b8=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',command=lambda :btnclick(8)).grid(row=1,column=1)
b9=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',command=lambda :btnclick(9)).grid(row=1,column=2)
add=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='+',command=lambda :btnclick("+")).grid(row=1,column=3)

b4=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',command=lambda :btnclick(4)).grid(row=2,column=0)
b5=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',command=lambda :btnclick(5)).grid(row=2,column=1)
b6=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',command=lambda :btnclick(6)).grid(row=2,column=2)
sub=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='-',command=lambda :btnclick("-")).grid(row=2,column=3)

b1=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',command=lambda :btnclick(1)).grid(row=3,column=0)
b2=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',command=lambda :btnclick(2)).grid(row=3,column=1)
b3=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',command=lambda :btnclick(3)).grid(row=3,column=2)
mulitply=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='*',command=lambda :btnclick("*")).grid(row=3,column=3)

b0=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',command=lambda :btnclick(0)).grid(row=4,column=0)
bclear=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='C',command= btncleardisplay).grid(row=4,column=1)
bequal=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',command=
              btnequalInput).grid(row=4,column=2)
division=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='/',command=lambda :btnclick("/")).grid(row=4,column=3)
cal.mainloop()
