from tkinter import *
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillClass
import sqlite3
from tkinter import messagebox
import os
import tempfile
import time

# from supplier import supplierClass
from PIL import Image,ImageTk
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
        self.filepath = "logo2.png"
        ##title
        im = Image.open(self.filepath)
        im=im.resize((50, 50))
        ph = ImageTk.PhotoImage(im)
        label = Label(root, image=ph)
        label.image=ph
        title=Label(self.root,text="WAREHOUSE MANAGEMENT SYSTEM",image=label.image,compound=LEFT,font=("Abolition",35,"bold"),bg="#010c78",fg="white",anchor="w",padx=25).place(x=0,y=0,relwidth=10,height=70)
        ##logout
        btnlogout=Button(self.root,text="Logout",font=("Abolition",15,"bold"),bg="yellow",fg="black",cursor="hand2").place(x=1150,y=20,height=30,width=150)
        ##clock
        self.lbl_clock=Label(self.root,text="Welcome to Warehouse Management system\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",compound=LEFT,font=("Times New Roman",15),bg="#010c48",fg="white",padx=25)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        ##left menu
        self.MenuLogo=Image.open("elem.png")
        self.MenuLogo=self.MenuLogo.resize((200,150))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        btn_menu=Button(LeftMenu,text="Menu",font=("Abolition",15),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("Abolition",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=("Abolition",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,font=("Abolition",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,font=("Abolition",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=("Abolition",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Manage Orders",command=self.billing,font=("Abolition",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=self.exit,font=("Abolition",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        ##content
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",font=("goudy old style",15),bd=5,relief=RIDGE,bg="#33bbf9",fg="white")
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",font=("goudy old style",15),bd=5,relief=RIDGE,bg="#ff5722",fg="white")
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[0]",font=("goudy old style",15),bd=5,relief=RIDGE,bg="#009688",fg="white")
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[0]",font=("goudy old style",15),bd=5,relief=RIDGE,bg="#607d8b",fg="white")
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",font=("goudy old style",15),bd=5,relief=RIDGE,bg="#ffc107",fg="white")
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        ##footer
        lbl_footer=Label(self.root,text="WMS - Warehouse Management System - DBS PROJECT\n For any queries contact",compound=LEFT,font=("Abolition",12,"bold"),bg="#010c48",fg="white").pack(side=BOTTOM,fill=X)
        self.update_con()
#===================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
    
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)

    def exit(self):
        exit()

        
    def update_con(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total  Products\n [{str(len(product))}]")
            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n [{str(len(supplier))}]")
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Categories\n [{str(len(category))}]")
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Product\n [{str(len(employee))}]")

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')

        
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Warehouse Management system\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_con)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : [{str(ex)}]")
        
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
