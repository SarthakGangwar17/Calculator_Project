
from tkinter import *

firstN=secondN=operator=None

def getOperator(a):
    global  firstN , operator
    firstN=int(rLabel['text'])

    operator=a

    rLabel.config(text='')

def result():
    global secondN
    secondN=int(rLabel['text'])
    if operator=='+':

        rLabel.config(text=str(firstN+secondN))

    elif operator=='-':

        rLabel.config(text=firstN-secondN)

    elif operator=='*':

        rLabel.config(text=firstN*secondN)

    elif operator=='/':
        if secondN !=0:

            rLabel.config(text=firstN/secondN)
        else:
            rLabel.config(text='Error')


def f(v):

    current=rLabel['text']
    new=current+str(v)
    rLabel.config(text=new)


def clear(v):
    rLabel.config(text='')

r =Tk()
r.title("Calculator")
r.geometry('310x447')
r.resizable(0,0)
r.configure(background='black')
rLabel=Label(r,text='' ,bg ='black',fg='white')
rLabel.grid(row=0,column=0,pady=(11,11),columnspan=1000,sticky='w')
rLabel.config(font=('verdana',35,'bold'))

buton7=Button(r,text=7,bg='white',fg='black',width=8,height=5,command=lambda  :f(7))
buton7.grid(row=1,column=0)
buton7.config(font=('verdana',10,'bold'))

buton8=Button(r,text=8,bg='white',fg='black',width=8,height=5,command=lambda  :f(8))
buton8.grid(row=1,column=1)
buton8.config(font=('verdana',10,'bold'))


button9=Button(r,text=9,bg='white',fg='black',width=8,height=5,command=lambda  :f(9))
button9.grid(row=1,column=2)
button9.config(font=('verdana',10,'bold'))

button4=Button(r,text=4,bg='white',fg='black',width=8,height=5,command= lambda :f(4))
button4.grid(row=2,column=0)
button4.config(font=('verdana',10,'bold'))

button5=Button(r,text=5,bg='white',fg='black',width=8,height=5, command=lambda :f(5))
button5.grid(row=2,column=1)
button5.config(font=('verdana',10,'bold'))

button6=Button(r,text=6,bg='white',fg='black',width=8,height=5, command= lambda :f(6))
button6.grid(row=2,column=2)
button6.config(font=('verdana',10,'bold'))


button1=Button(r,text=1,bg='white',fg='black',width=8,height=5 , command= lambda :f(1))
button1.grid(row=3,column=0)
button1.config(font=('verdana',10,'bold'))

button2=Button(r,text=2,bg='white',fg='black',width=8,height=5, command= lambda :f(2))
button2.grid(row=3,column=1)
button2.config(font=('verdana',10,'bold'))

button3=Button(r,text=3,bg='white',fg='black',width=8,height=5 , command = lambda : f(3))
button3.grid(row=3,column=2)
button3.config(font=('verdana',10,'bold'))

buttonC=Button(r,text='C',bg='white',fg='black',width=8,height=5, command= lambda : clear('C'))
buttonC.grid(row=4,column=0)
buttonC.config(font=('verdana',10,'bold'))

button0=Button(r,text=0,bg='white',fg='black',width=8,height=5,command= lambda  : f(0))
button0.grid(row=4,column=1)
button0.config(font=('verdana',10,'bold'))

buttonEqualto=Button(r,text='/',width=6,height=5,bg='Dark Orange',fg='black' , command= lambda :getOperator('/'))
buttonEqualto.grid(row=4,column=3)
buttonEqualto.config(font=('verdana',10,'bold'))



buttonDivide=Button(r,text='=',bg='Dark Orange',fg='black',width=8,height=5,command= lambda :result())
buttonDivide.grid(row=4,column=2)
buttonDivide.config(font=('verdana',10,'bold'))

buttonPlus=Button(r,text='+',bg='Dark Orange',fg='black',width=6,height=5,command= lambda :getOperator('+'))
buttonPlus.grid(row=1,column=3)
buttonPlus.config(font=('verdana',10,'bold'))

buttonSubtraction=Button(r,text='-',bg='Dark Orange',fg='black',width=6,height=5,command= lambda :getOperator('-'))
buttonSubtraction.grid(row=2,column=3)
buttonSubtraction.config(font=('verdana',10,'bold'))
#
buttonMultiplication=Button(r,text='x',bg='Dark Orange',fg='black',width=6,height=5,command= lambda :getOperator('*'))
buttonMultiplication.grid(row=3,column=3)
buttonMultiplication.config(font=('verdana',10,'bold'))


r.mainloop()
