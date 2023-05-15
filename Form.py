from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk, messagebox
import sqlite3

#GUI_Designing

class CRUDClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("830x370+200+130")
        self.root.title("Gestion de stock")
        self.root.config(bg="white")

        #self.root.focus_force()
        self.root.resizable(0,0)

        #-All variables

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_loginId=StringVar()
        self.var_uName=StringVar()
        self.var_password=StringVar()
        self.var_address=StringVar()

        #label
        lbl_title=Label(self.root, text="stock", font=("Arial", 20, "bold"), fg="#0f4d7d").place(x=15, y=20, width=800,height=40)
        lbl_search=Label(self.root,text="SearchByID", bg="white", font=("Arial",15)).place(x=390, y=80)
        lbl_loginId=Label(self.root, text="Id", font=("Arial", 15), bg="white").place(x=50,y=80)
        lb1_Uname=Label(self.root, text="User Name", font=("Arial", 15), bg="white").place(x=50, y=120)
        lbl_pass=Label(self.root, text="Password", font=("Arial", 15), bg="white").place(x=50, y=160)
        lbl_address=Label(self.root, text="Address", font=("Arial", 15), bg="white").place(x=50, y=200)
        #Textbox
        txt_search=Entry(self.root, textvariable=self.var_searchtxt, font=("Arial",15), bg="white").place(x=505, y=80, width=160)
        txt_loginId=Entry(self.root, textvariable=self.var_loginId, font=("Arial",15), bg="white").place(x=180, y=80, width=180)
        txt_Uname=Entry(self.root, textvariable=self.var_uName, font=("Arial",15), bg="white").place(x=180,y=120, width=180)
        txt_pass=Entry(self.root, textvariable=self.var_password, show="*", font=("Arial",15), bg="white").place(x=180, y=160, width=180)
        txt_Address=Entry(self.root, textvariable=self.var_address, font=("Arial", 15), bg="white").place(x=180, y=200, width=180)
        #Buttons
        btn_search=Button(self.root, text="Search", font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=700, y=79,width=100,height=30)
        btn_add=Button(self.root,text="Save",command=self.Save, font=("Times New Roman", 15), bg="#2196f3",fg="white", cursor="hand2").place(x=180, y=250,width=110,height=30)
        btn_update=Button(self.root, text="Update", font=("Times New Roman",15), bg="#4caf50",fg="white", cursor="hand2").place(x=300,y=250,width=110,height=30)
        btn_delete=Button(self.root, text="Delete", font=("Times New Roman",15), bg="#f44336",fg="white", cursor="hand2").place(x=180, y=300,width=110,height=30)
        btn_clear=Button(self.root, text="clear",command=self.Save, font=("Times New Roman",15), bg="#607d8b",fg="white", cursor="hand2").place(x=300, y=300,width=110, height=30)

        #User_Details
        emp_frame=Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=420, y=120,width=380,height=215)
        #Scrollbar
        scrolly=Scrollbar (emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)
        #================CreatingTableView=======
        self.supplierTable=ttk.Treeview(emp_frame, columns=("login_Id", "Uname", "password","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("login_Id",text="ID")
        self.supplierTable.heading("Uname", text="User Name")
        self.supplierTable.heading("password", text="Password")
        self.supplierTable.heading("address",text="Address")
        self.supplierTable["show"]="headings"
        self.supplierTable.column("login_Id",width=50)
        self.supplierTable.column("Uname",width=100)
        self.supplierTable.column("password",width=100)
        self.supplierTable.column("address",width=100)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        #DatabaseConnection

    def connection ():
        con = sqlite3.connect(database='login.db')
        cur = con.cursor()
        


        #== -SaveForSQLite===
    def Save(self):
        connection
        try:
            if self.var_loginId.get()=="":
                messagebox.showerror("Error", "Id must be required",parent=self.root)
            else:
                cur.execute("Select * from Login where login_Id=?", (self.var_loginId.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Id already exits, Try different",parent=self.root)
                else:
                    cur.execute("Insert into Login (Uname, password, address) values (?, ?, ?)",(
                                        self.var_uName.get(),
                                        self.var_password.get(),
                                        self.var_address.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "New User Added Sucessfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)
            

#ShowDatForSQLite=======
    def show(self):
        connection
        try:
            cur.execute("select * from Login")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
#GetDataForSQLite
    def get_data(self,ev):
            f=self.supplierTable.focus()
            content=self.supplierTable.item(f)
            row=content['values']
            # print (row)
            self.var_loginId.set(row[0]),
            self.var_uName.set(row[1]),
            self.var_password.set(row [2]),
            self.var_address.set(row[3])

# UpdateForSQLite======
    def update(self):
        connection
        try:
            if self.var_loginId.get()=="":
                messagebox.showerror("Error", "Id must be required",parent=self.root)
            else:
                cur.execute("Select * from Login where login_Id=?", (self.var_loginId.get(), ))
                row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid ID",parent=self.root)
            else:
                cur.execute("Update Login set Uname=?, password=?, address=? where login_Id=?",(
                                    self.var_uName.get(),
                                    self.var_password.get(),
                                    self.var_address.get(),
                                    self.var_loginId.get()
                ))
                con.commit()
                messagebox.showinfo("Sucess", "User Updated Sucessfully" ,parent=self.root)
                self.clear()
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)

            #=== =====DeleteForSQLite======
    def delete(self):
        connection
        try:
            if self.var_loginId.get()=="":
                messagebox.showerror("Error", "ID must be required",parent=self.root)
            else:
                cur.execute("Select * from Login where login_Id=?", (self.var_loginId.get(), ))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid ID",parent=self.root)
                else:
                    cosM=messagebox.askyesno ("Confirm", "Do you want to delete",parent=self.root)
                    if cosM==True:
                        cur.execute("delete from Login where login_Id=?", (self.var_loginId.get(), ))
                        con.commit()
                        messagebox.showinfo("Delete", "User Delete Successfully",parent=self.root)
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
#==== ===ClearForSQLite======
    def clear(self):
        self.var_loginId.set(""),
        self.var_uName.set(""),
        self.var_password.set(""),
        self.var_address.set(""),
        self.var_searchtxt.set("")
        self.show()
# ======SearchForSQLite=======‒‒‒‒‒‒‒‒‒‒‒‒‒‒
    def search(self):
        connection
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Id should be required.",parent=self.root)
            else:
                cur.execute("select * from Login where login_Id=?", (self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)


#DatabaseConnection
con = sqlite3.connect(database='login.db')
cur = con.cursor()
def connection ():
    cur.execute("CREATE TABLE IF NOT EXISTS Login (login_Id INTEGER PRIMARY KEY AUTOINCREMENT, UName VARCHAR(100), password VARCHAR(100), address VARC(100))")
    con.commit()
    connection()


    

    #MainMethod

if __name__ =="__main__":
    root=Tk()
    obj=CRUDClass(root)
    root.mainloop()