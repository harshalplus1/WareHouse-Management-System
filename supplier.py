from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
        self.root.config(bg="white")
        self.root.focus_force()
        #all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()

        ##===search frame

        ##options
        lbl_search=Label(self.root,text="Invoice No.",font=("goudy old style",15))
        lbl_search.place(x=700,y=60)

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=810,y=60,height=25,width=180)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=1000,y=60,height=25,width=70)
        ##title
        title=Label(self.root,text="Supplier Details",font=("goudy old style",15),bd=5,relief=RIDGE,bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)
        #content
        ##row1
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=60)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=60,width=200)
        ##row2
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=200)
        ##row3
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=180,width=200)
        ##row4
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=250)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=250,width=500,height=90)
        ##buttons
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=400,height=28,width=110)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=305,y=400,height=28,width=110)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=430,y=400,height=28,width=110)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=555,y=400,height=28,width=110)



        ###table
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=90,width=400,height=410)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.suppliertable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.suppliertable.xview)
        scrolly.config(command=self.suppliertable.yview)
        self.suppliertable.heading("invoice",text="Invoice")
        self.suppliertable.heading("name",text="Name")
        self.suppliertable.heading("contact",text="Contact")
        self.suppliertable.heading("desc",text="Description")
        
        self.suppliertable["show"]="headings"

        self.suppliertable.column("invoice",width=90)
        self.suppliertable.column("name",width=90)
        self.suppliertable.column("contact",width=90)
        self.suppliertable.column("desc",width=90)

        self.suppliertable.pack(fill=BOTH,expand=1)
        self.suppliertable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        # ==================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice no. is already assigned, try Different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                    self.var_sup_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0',END),
                                    self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    def delete(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_sup_invoice.get()=="":
                    messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
                else:
                    cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                    else:
                        op=messagebox.askyesno("Confirm","Do you want to delete ?",parent=self.root)
                        if op==True:
                            cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                            con.commit()
                            messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root) 
                            self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.suppliertable.delete(*self.suppliertable.get_children())
            for row in rows:
                self.suppliertable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        f=self.suppliertable.focus()
        content=(self.suppliertable.item(f))
        row=content['values']
        # print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. is required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:      
                    self.suppliertable.delete(*self.suppliertable.get_children())
                    self.suppliertable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
        #=============================
if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()
