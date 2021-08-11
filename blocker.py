from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk,Image
import tkinter as tk
import website_blocker
from tkinter import messagebox

def addToList():
    website= entry_var.get()  
    if "www."not in website:  
        website = "www."+website
    website_blocker.addWebsite(website) 
    
    website_blocker.block(0)  


def view_blocked():
     list_box.delete(0,END)  
     
     for rows in website_blocker.blocked_list():
         list_box.insert(END,rows) 
   


selected_row = None 
def get_selected_row(event): 
    global selected_row
    try:
        index = list_box.curselection()[0]  
        selected_row = list_box.get(index)  
        website.delete(0,END)
        website.insert(END,selected_row)    
    except:
        IndexError          


def unblock():
    website = entry_var.get()  
    website_blocker.block(1)
    website_blocker.deleteWebsite(selected_row[0])

def adsblock():
    messagebox.showerror("I am sorry","Under Construction")

window = Tk()
window.geometry("1000x500")
window.resizable(0,0)
image=Image.open("F:\\My doc\\website_blocker-master\\car.jpg")
photo=ImageTk.PhotoImage(image)
website_label = Label(window,image=photo)
website_label.place(x = 0, y = 0)
label=Label(window,text="Website:" ,font=("arial",15,"bold"))    
label.place(x = 100 , y = 50)    
entry_var = StringVar()  
website = Entry(window,width = 53,fg="blue",bg="lightgray",font=("arial",15,"bold"),textvariable=entry_var) 
website.place(x = 200,y = 50)

block = Button(window,text = "Block",fg="blue",bg="red",font=("arial",12,"bold"),width = 10,command = addToList)
unblock = Button(window,text = "UnBlock",fg="blue",bg="green",font=("arial",12,"bold"),width = 10,command=unblock)
view_block = Button(window,text = "View Blocked",fg="red",bg="blue",font=("arial",12,"bold"),width = 10,command = view_blocked)
close = Button(window,text = "Close",fg="blue",bg="yellow",font=("arial",12,"bold"),width = 10,command=exit)
adblock = Button(window,text = "Block ads",fg="indigo",bg="peachpuff",font=("arial",12,"bold"),width = 10,command=adsblock)
        
block.place(x = 210, y = 100)
unblock.place(x = 340 , y = 100)
view_block.place(x = 470, y = 100)
close.place(x = 600, y = 100)
#adblock.place(x = 690 , y = 100) 

list_box = Listbox(window,width = 65,fg="blue",bg="gold",font=("arial",12,"bold"))
list_box.place(x = 200, y = 150,height = 200)

list_box.bind('<<ListboxSelect>>',get_selected_row)  
        
window.mainloop()
