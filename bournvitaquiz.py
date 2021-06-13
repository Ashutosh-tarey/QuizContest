import tkinter 
import random
import tkinter.messagebox
import webbrowser
from tkinter import *

questions=[
"Where will the next Olympic Games be held, and when?",
"Who are the founders of Google?",
"When is the International Yoga Day celebrated?",
"Who among the following considered as the 'father of artificial intelligence'?",
"Which of the following is also called translator?",
"Who is the author of the novel ‘The Inheritance of Loss’?",
"Country whose National Anthem has only music not words is?",
"Which among the following is the oldest dynasty?",
"Who discovered the Symbol Infinity “∞”?",
"Who was the First india's Sportsperson to Receive the Padma Vibhushan Award?",
]

answers_choice=[
["Tokyo,2021","London,2012","Los Angeles,1984","Moscow,1980",],
["Peirre Curie,Marie Curie","Henry Duckworth,Tony Lewis","Larry Page,Sergey Brin","Louis Pasteur and Alexander Fleming",],
["17 December","21 June","3 February","24 March",],
["Charles Babbage","Lee De Forest","John McCarthy","JP Eckert",],
["Data representation","MS-DOS","Operating System","Language Processor",],
["Amitav Ghosh"," Arundhati Roy","Kiran Desai","None of these",],
["India"," Bahrain","Germany","Spain",],
["Maurya","Gupta","Kushan","Kanva",],
["Robert Recorde","Leonardo Pisano Bigollo","William Jones","John Wallis",],
["Abhinav Bindra","Vishwnathan Anand","Leander Peas","Magnus Carlsen",],
]

actual_answer=[0,2,1,2,3,2,2,0,3,1]

chosen_answers=[]
a=[]



url = "https://www.facebook.com/BournvitaQuizContest/"

def gotothecontest():
    webbrowser.open_new_tab(url)


def submit():
    messagebox.showinfo('submit','Your Response Has Been Recorded!')


def adding():
    global a
    while(len(a)<10):
        x=random.randint(0,9)
        if x in a:
            continue
        else:
            a.append(x)
    print(a)
def showresult(score):
    
    label1.destroy()
    label7.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    
    label9=Label(root,relief=GROOVE,font=("Arial",20),border=0)
    label11=Label(root,font=("Comic Sans MS",18,"italic"),background="#ffffff",)
    label12=Label(root,font=("Comic Sans MS",12,"italic"))
    label10=Label(root,font=("Comic Sans MS",20,"italic","bold"),background="#ffffff")
    l = Label(root, text = "Please, Give your Feedback")
    l1=Label(root,width=100,padx=10) 
    Txtbox = Text(root, height = 5, width = 52)
    b1 = Button(root, text = "Submit",command = submit,font=("Comic Sans MS",12,"italic"),bd=1)
    b2 = Button(root, text = "Exit",command = root.destroy,font=("Comic Sans MS",12,"italic"))
    Btn = Button(root, text = "Visit Our Page",command=gotothecontest,font=("Comic Sans MS",12,"italic"))
    
    label9.pack()
    label10.pack()
    label11.pack()
    label12.pack()
    l.pack()
    Txtbox.pack() 
    b1.pack(pady=10)
    b2.pack(pady=10)
    Btn.pack()
    l1.pack()
    img=PhotoImage(file="images.png")
    
    if score>=70:
        x=int(score/10)
        y=int(10 - (score/10))
        a=str(x)
        b=str(y)
        res=str(score)
        label9.configure(image=img)
        label9.image=img
        label11.configure(text="Well Done!! You have Scored "+res+" Out of 100.",pady=10,relief=GROOVE)
        label12.configure(text="Here is Your Performace Chart:\nYou Have Scored "+a+" Correct and "+b+" Incorrect Questions",pady=30,background="#ffffff")
        l.config(font =("Comic Sans MS",18,"italic"),relief=GROOVE)
    if score<70:
        label10.configure(text="Your Performance wasen't up to the Mark and \nYou haven't Passed the Test Successfully.",pady=10,background="yellow",relief=RAISED)
        label11.configure(text="Bad Luck!! You have not Scored Well in the Test ,\n We Wish You the Best Of Luck For Your Future.",relief=GROOVE)
        l.config(font =("Comic Sans MS",18,"italic"))
def calc():
    global a,chosen_answers,actual_answer
    x=0
    score=0
    for i in a:
        if chosen_answers[x]==actual_answer[i]:
            score+=10
        x+=1
    print(score)    
    showresult(score)


def ispressed():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label5.destroy()
    label6.destroy()
    btn1.destroy()    
    adding()
    quizbegin()

ques=1
def selected():
    global radiovar,chosen_answers
    global label7,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    chosen_answers.append(x)
    radiovar.set(-1)
    if ques<10:
        label7.config(text=questions[a[ques]])
        r1['text']=answers_choice[a[ques]][0]
        r2['text']=answers_choice[a[ques]][1]
        r3['text']=answers_choice[a[ques]][2]
        r4['text']=answers_choice[a[ques]][3]
        ques+=1
    else:
        print(a)
        print(chosen_answers)
        calc()
        pass

def quizbegin():
    global label7
    global r1,r2,r3,r4
    label7=Label(root,background="brown",relief=GROOVE,text=questions[a[0]],font=("Comic Sans MS",20,"italic"),width=500,justify="center",wraplength=400)
    label7.pack()
    
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)    
    
    r1=Radiobutton(root,text=answers_choice[a[0]][0],value=0,variable=radiovar,command=selected)
    r1.pack(pady=20,fill=X)

    r2=Radiobutton(root,background="light blue",text=answers_choice[a[0]][1],value=1,variable=radiovar,command=selected)
    r2.pack(pady=10,fill=X)

    r3=Radiobutton(root,text=answers_choice[a[0]][2],value=2,variable=radiovar,command=selected)
    r3.pack(pady=10,fill=X)

    r4=Radiobutton(root,background="light blue",text=answers_choice[a[0]][3],value=3,variable=radiovar,command=selected)
    r4.pack(pady=10,fill=X)






root=tkinter.Tk()
root.title("Bournvita-Quiz Contest")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)


img= PhotoImage(file="download.png")

label1=Label(root,image=img,relief=RAISED,border=5)
label2=Label(root,text="BournVita- QuizContest",font=("Comic Sans MS",20,"bold"),background="#ffffff")
label3=Label(root,text="This Test Contains 10 Questions ! Each Question Carries 10 Marks !",font=("Comic Sans MS",12,"bold"),pady=10,relief=GROOVE)
btn1=Button(root,text="PRESS HERE",font=("Comic Sans MS",12,"bold"),relief=GROOVE,width=15,command=ispressed)
label5=Label(root,text="Read the Rules and Click Start When You Are Ready.",font=("Comic Sans MS",16,"bold"),background="#ffffff",justify="center")
label6=Label(root,text="You will Get Four \n RadioButtons for One Question,\nOnce you select ,that will be your Final Choice,\n So Choose Very Carefully.",width=100,font=("Comic Sans MS",12,"bold"))

label1.pack()
label2.pack(pady=3)
label3.pack()
btn1.pack(pady=40)
label5.pack()
label6.pack(pady=10)



root.mainloop()
