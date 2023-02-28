#MIHIR CHAVAN 201080021 IT 
from tkinter import *
from tkinter import ttk,messagebox
import os #To use startfile() function
root=Tk() #Tk class is used to create a root window
root.title('Employee management system')#Title of tkinter window
root.geometry('1280x820')
bg_color='#3333FF'#background Color in Hexcode format

#======================Variable====================#
ref_var=IntVar() #variable for employee ref number
name_var=StringVar()#variable for employee name
gender_var=StringVar()
email_var=StringVar()
salary_var=IntVar()
phone_var=IntVar()
desi_var=StringVar()
##
pan_var=IntVar()
adh_var=IntVar()


#======================Functions=====================#

def add(): #definition of add button/function
    if ref_var.get()==0 or name_var.get()=='' or salary_var.get()=='' or gender_var=='' or email_var=='' or desi_var=='' or phone_var==''or  pan_var==0 or adh_var==0 :
        messagebox.showerror('Error','All fields are required') #Will show error if all fields are not filled
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, '\n==============================================')
        textarea.insert(END,f'Employee Ref\t\t\t\t{ref_var.get()}')
        textarea.insert(END, '\n==============================================')
        textarea.insert(END,f'\nEmployee Name\t\t\t\t{name_var.get()}')
        textarea.insert(END,f'\nEmail Id\t\t\t\t{email_var.get()}')
        textarea.insert(END,f'\nGender\t\t\t\t{gender_var.get()}')
        textarea.insert(END,f'\nDesignation\t\t\t\t{desi_var.get()}')
        textarea.insert(END,f'\nSalary\t\t\t\t{salary_var.get()}')
        textarea.insert(END,f'\nAddress\t\t\t\t{txt_add.get()}')
        textarea.insert(END,f'\nPan No: \t\t\t\t{pan_var.get()}')
        textarea.insert(END,f'\nAdhaarNo:\t\t\t\t{adh_var.get()}')

def save(): #definition of save button/function
    data=textarea.get(1.0,END)
    f1=open('D:\Mihir docs C to d Drive\Desktop Files\Python vs code\Pdl_Proj\\'+str(ref_var.get())+'.txt','w')
    f1.write(data) #File will be saved only if correct address of folder in which it is to be saved is provide which will be different for all PCs
    f1.close()
    messagebox.showinfo('Saved',f'Ref No:{ref_var.get()} Saved Successfully')

def print(): #definition of Print button/function
    data=textarea.get(1.0,END)
    f='D:\\Mihir docs C to d Drive\\Desktop Files\\Python vs code\\Pdl_Proj\\'+str(ref_var.get())+'.txt'
    os.startfile(f,'Print') #File will be printed only if correct address of folder in which it is to be printed is provide which will be different for all PCs
    #The os.startfile() method allows us to “start” a file with its associated program. 

def reset(): #definition of reset button/function
    textarea.delete(1.0,END)
    txt_add.delete(1.0,END)
    ref_var.set(0)
    name_var.set('')
    gender_var.set('')
    desi_var.set('')
    phone_var.set('')
    email_var.set('')
    salary_var.set('')
    pan_var.set(0)
    adh_var.set(0)

def Exit(): #definition of exit button/function
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()



#======================Heading=====================#
title=Label(root,text='Employee Record System',bg=bg_color,fg='white',font=('times new rommon',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X) #Accomaodates itself on x axis
#Title of inner window/output page

#======================Left Frame==================#
F1=Frame(root,bg=bg_color,relief=RIDGE,bd=15) #Information of 1st frame on left side
F1.place(x=10,y=80,width=650,height=720)

#Creating Labels and text boxes/drop down menus to fill details in left frame
lbl_ref=Label(F1,text='Employee Reference',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_ref.grid(row=0,column=0,padx=30,pady=10)
txt_ref=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=ref_var)#Creating text boxes
txt_ref.grid(row=0,column=1,pady=10,sticky='w')

lbl_name=Label(F1,text='Employee Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_name.grid(row=1,column=0,padx=30,pady=10)
txt_name=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=name_var)
txt_name.grid(row=1,column=1,pady=10,sticky='w')

lbl_email=Label(F1,text='Employee Email',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_email.grid(row=2,column=0,padx=30,pady=10)
txt_email=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=email_var)
txt_email.grid(row=2,column=1,pady=10,sticky='w')

lbl_gender=Label(F1,text='Gender',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_gender.grid(row=3,column=0,padx=30,pady=10)
combo_gender=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=gender_var)#state is 'readonly' to avoid random user input
combo_gender['value']=('Male','Female') #Creating drop down menu to choose selected options only
combo_gender.grid(row=3,column=1,pady=10)

lbl_des=Label(F1,text='Designation',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_des.grid(row=4,column=0,padx=30,pady=10)
combo_des=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=desi_var)
combo_des['value']=('Hr','IT','Sales','Marketing','Finanace','Quality Check','R&D')
combo_des.grid(row=4,column=1,pady=10)

lbl_no=Label(F1,text='Mobile Number',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_no.grid(row=5,column=0,padx=30,pady=10)
txt_no=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=phone_var)
txt_no.grid(row=5,column=1,pady=10,sticky='w')

lbl_s=Label(F1,text='Salary',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_s.grid(row=6,column=0,padx=30,pady=10)
txt_s=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=salary_var)
txt_s.grid(row=6,column=1,pady=10,sticky='w')

lbl_add=Label(F1,text='Address',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_add.grid(row=7,column=0,padx=30,pady=10)
txt_add=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
txt_add.grid(row=7,column=1,pady=10,sticky='w')


######
lbl_ref1=Label(F1,text='Pan NO ',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_ref1.grid(row=8,column=0,padx=30,pady=10)
txt_ref1=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=pan_var)#Creating text boxes
txt_ref1.grid(row=8,column=1,pady=10,sticky='w')


lbl_ref2=Label(F1,text='Adhaar NO ',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_ref2.grid(row=9,column=0,padx=30,pady=10)
txt_ref2=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=adh_var)#Creating text boxes
txt_ref2.grid(row=9,column=1,pady=10,sticky='w')





#======================Right Frame==================#
F2=Frame(root,bg=bg_color,relief=RIDGE,bd=15) #Information of 2nd frame on right side
F2.place(x=665,y=80,width=610,height=720)

lbl_t=Label(F2,text='Employee Details',font=('arial',20,'bold'),fg='black',bd=7,relief=GROOVE)#Label of right frame
lbl_t.pack(fill=X)
scroll=Scrollbar(F2,orient=VERTICAL)#Creating a scroll bar for right frame
scroll.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scroll.set)
textarea.pack(fill=BOTH)
scroll.config(command=textarea.yview)

#======================Buttons==================#
F3=Frame(root,bg=bg_color,relief=RIDGE,bd=15) #creating 3rd frame at the bottom
F3.place(x=10,y=730,width=1260,height=100)

btn1=Button(F3,text='Add Record',font='aril 20 bold',bg='yellow',fg='crimson',command=add)#Add Record button created
btn1.grid(row=0,column=0,padx=50,pady=7)


btn2=Button(F3,text='Save',font='aril 20 bold',bg='yellow',fg='crimson',command=save) #Save button created
btn2.grid(row=0,column=1,padx=50,pady=7)


btn3=Button(F3,text='Print',font='aril 20 bold',bg='yellow',fg='crimson',command=print)#Print button created
btn3.grid(row=0,column=2,padx=50,pady=7)


btn4=Button(F3,text='Reset',font='aril 20 bold',bg='yellow',fg='crimson',command=reset) #Reset button created
btn4.grid(row=0,column=3,padx=50,pady=7)


btn5=Button(F3,text='Exit',font='aril 20 bold',bg='yellow',fg='crimson',command=Exit) #Exit button created
btn5.grid(row=0,column=4,padx=50,pady=7)



root.mainloop()