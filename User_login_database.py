# database creator for the user login program
from tkinter import *
import sqlite3
root = Tk()






# Create table three commas allow for multiline command only need to create once, then keep the code part idle
'''dtbse.execute("""CREATE TABLE  (
		User_ID text,
		password text) 
	""")'''
#what will happen?
def submit_action():

	# make or connect to a database
	the_database = sqlite3.connect('User_login_database.db')
	# adding the cursor to the made database, it does stuff for us
	cursor_log = the_database.cursor()

	# doing the task
	cursor_log.execute("""INSERT INTO User_data VALUES ( :first_name_info, :Last_Name_info)""",
		
		{'first_name_info': User_ID_Entry.get(),
		'Last_Name_info': password_Entry.get()

		})





	# 'commit' changes
	the_database.commit()

	# to end connection
	the_database.close()

	# deleting the previous data
	User_ID_Entry.delete(0, END)
	password_Entry.delete(0, END)



# what to show?
def Query_action():
	dtbse = sqlite3.connect('User_login_database.db')
	cursor = dtbse.cursor()
	cursor.execute(" SELECT *, oid FROM User_data")
	records = cursor.fetchall()
	#looping to diplay better-ly

	print_records = ' ' 
	for record in records[0 : len(records)]:
		print_records += str(record) + "\n"

	output_label =Label(root, text = print_records)
	output_label.grid(row=4, column=0,columnspan=2,padx=10,pady=20)




	dtbse.commit()
	dtbse.close()
	


# creating text Labels

Label0 = Label(root, text = "   User ID: ").grid(row = 0,column = 0)
Label1 = Label(root, text = "  Password: ").grid(row = 1,column = 0)


# creating Entry boxes

User_ID_Entry = Entry( root, width = 20, borderwidth = 5)
User_ID_Entry.grid( row=0 , column=1)

password_Entry = Entry( root, width = 20, borderwidth = 5)
password_Entry.grid( row=1 , column=1)




# creating the insert button

Submit_button = Button(root, text='Submit data', command = submit_action)
Submit_button.grid(row=2,column=0,columnspan=2,padx=10,pady=10,ipadx=120)

# creating show data button

Query_button = Button(root, text='Show records', command= Query_action)
Query_button.grid(row=3, column =0,columnspan=2,padx=10,pady=10,ipadx=120)






root.mainloop()