from tkinter import *
# from PIL import ImageTk,Image
import sqlite3

root = Tk()

# Program Name
root.title("Task Tracker")
# root.iconbitmap('C:/Users/Owner/Desktop/coding/Task Tracker/icon.ico')

# Size of popup window
root.geometry("500x935")

# Create a database or connect to one
conn = sqlite3.connect('task_log.db')

# Create cursor
c = conn.cursor()

# Create table named taskslist
'''
c.execute("""CREATE TABLE tasklist (
		task text,
		minutes integer)""")
'''

# Create Delete function for database
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('task_log.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from tasklist WHERE oid = " + delete_box.get())

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create Submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('task_log.db')
    # Create cursor
    c = conn.cursor()

    # Insert into Table 
    c.execute("INSERT INTO tasklist VALUES (:task, :minutes)",
            {
                'task': task.get(),
                'minutes': minutes.get()
            })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear the text boxes
    task.delete(0, END)
    minutes.delete(0, END)

# Create Query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('task_log.db')
    # Create cursor
    c = conn.cursor()
    # Query the database (select everything in tasklist)
    c.execute("SELECT *, oid FROM tasklist")  
    # Fetch all records
    records = c.fetchall()

    # Loop Through Results
    print_records = ''
    for record in records:
        # This is how records are displayed. record[0] = task, record [1] = minutes
        print_records += str(record[0]) + " for " + str(record[1]) + " minutes." + "\t" + str(record[2]) + "\n" 

    query_label = Label(root, text = print_records)
    query_label.grid(row = 7, column = 0, columnspan = 2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

# Create Text Boxes
task = Entry(root, width = 60)
task.grid(row = 0, column = 1, padx = 10, pady = (10,0)) #pady (x,y) to add padding to top

minutes = Entry(root, width = 60)
minutes.grid(row = 1, column = 1, padx = 10)

delete_box = Entry(root, width = 60)
delete_box.grid(row = 5, column = 1)

# Create Text Box Labels
task_label = Label(root, text = "Task")
task_label.grid(row = 0, column = 0, pady = (10,0))

minutes_label = Label(root, text = "Minutes on Task")
minutes_label.grid(row = 1, column = 0)

delete_box_label = Label(root, text = "Select Record")
delete_box_label.grid(row = 5, column = 0, pady = 5)

# Create Submit Button
submit_btn = Button(root, text = "Add Record to Database", command = submit)
submit_btn.grid(row = 2, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 111)

# Create a Query Button
query_btn = Button(root, text = "Show Records", command = query)
query_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# Create a Delete Button
delete_btn = Button(root, text = "Delete Record", command = delete)
delete_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 136)

# Command function of clicking button.
# Figure out how to input onto notepad to store data.
# def taskInput():
#    myLabel = Label(root, text = task.get())
#    myLabel.pack()

# Creating the button and the command once clicked.
# taskInput_button = Button(root, text="Input Task", command = taskInput)
# taskInput_button.grid(row = 1, column = 1)

# timeInput_button = Button(root, text="Minutes on Task", command = taskInput)
# timeInput_button.grid(row = 2, column = 1)

# Commit changes
conn.commit()

# Close connection
conn.close()

# myButton.pack()
root.mainloop()