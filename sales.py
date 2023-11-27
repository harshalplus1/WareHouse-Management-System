from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import os
class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System ")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice=StringVar()
        # title
        lbl_title=Label(self.root,text="View Customer Bills",font=("goudy old style",30),bd=3,relief=RIDGE,bg="#184a45",fg="white").pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_invoice=Label(self.root,text="Invoice No.",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_invoice,font=("goudy old style",18),bg="lightyellow").place(x=160,y=100,width=300)
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=100,width=120,height=32)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",fg="black",cursor="hand2").place(x=650,y=100,width=120,height=32)
#       list

        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=150,width=400,height=330)
        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)

        self.Sales_List=Listbox(sales_Frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)

        # bill area
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=550,y=150,width=400,height=330)
        lbl_title2=Label(bill_Frame,text="Customer Bill Area",font=("goudy old style",20),bg="orange").pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)

        self.bill_area=Text(bill_Frame,bg="lightyellow",yscrollcommand=scrolly2)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        self.show()
# ================================
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. is required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice Number",parent=self.root)


    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()