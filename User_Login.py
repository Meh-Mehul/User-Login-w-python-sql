#login into something but with database use

import sqlite3
from tkinter import *

root = Tk()
root.geometry('475x250+830+450')
root.title('User Login')

Login_label = Label(root, text="Please Login", font=('Arial', 20, 'bold')).grid(row=0,column=0,columnspan=3)

Dash_Label0 = Label(root, text="                                      ").grid(row= 1,column=0)

ID_label = Label(root, text="Enter User ID:     ", font=('Arial', 18, 'bold'))

ID_label.grid(row=2,column=0)

ID_Entry = Entry(root, width='23', borderwidth=7)
ID_Entry.grid(row=2,column=2)

Dash_Label1 = Label(root, text="                                      ").grid(row= 3,column=0)
Dash_Label2 = Label(root, text="                                      ").grid(row= 4,column=0)

Pass_label = Label(root, text="Enter Password:  ", font=('Arial', 18, 'bold'))
Pass_label.grid(row=5,column=0)

Pass_Entry = Entry(root, width='23', borderwidth=7)
Pass_Entry.grid(row=5,column=2)



def Login_click():
	# getting the needed data from the already made database
	Password_chk = Pass_Entry.get()
	string = ''
	i = 0
	while i < len(Password_chk):
		string +=  "*"
		i = i+1

	Pass_Entry.delete(first=0, last=22)
	Pass_Entry.insert(0, string)

	database = sqlite3.connect('User_login_database.db')
	cursor = database.cursor()
 



	cursor.execute(""" SELECT password FROM USer_data WHERE User_ID = :ID_check """,
		{
		'ID_check' : ID_Entry.get()
		})
	correct_password_list = cursor.fetchall()
	for item in correct_password_list[0] :
		correct_password = '' + item
	database.commit()
	database.close()

	# if-else check for correctness of password
	if Password_chk == str(correct_password) :
		root_true = Tk()
		root_true.title('Login Successful')
		happ = Label(root_true, text="yaayyy login is done").pack()
		def endlifetime():
			root_true.destroy()
		root_true.after(3000,endlifetime)
		
		root_true.mainloop()
	else :
		root_false = Tk()
		root_false.title('wrong!!')
		wrong = Label(root_false, text="Noooo cant login").pack()

		def endlifetime1():
			root_false.destroy()
		root_false.after(3000,endlifetime1)
		root_false.mainloop()


# defining the button to do it all
The_button = Button(root, text= "Login", padx= 45, pady= 15, font=('Arial', 15), command= Login_click).grid(row=6,column=0,columnspan= 3, padx=15,pady=15, ipadx=100)
root.mainloop()
