from tkinter import *
import sqlite3

root=Tk() 
#don't forget to loop the file with Tkinter
root.title("Ticket Please")
root.geometry("500x300")

#	LEGEND
#cc= Calling Company
#cca= Calling Compnay address
#cctel= calling compnay telephone number
#te= last tech dealing with ticket
#notes= case discription
#stats= case status
#mm= machine model
#msn=machine serial number

#Create a databese or connect to one
con=sqlite3.connect('ticket.db')
#Create a cursor that fetches and places
cur=con.cursor()

#Databases

#create Table 
cur.execute("""CREATE TABLE IF NOT EXISTS ticket (  
	calling_customer null, 
	address null, 
	telephone null, 
	tech null, 
	status null, 
	model null, 
	serial_number null, 
	notes null 
	)""")	

def new():
    new=Tk()
    new.title("Ticket Please")
    new.geometry("500x500")
    con=sqlite3.connect('ticket.db')
    cur=con.cursor()

#submit function
    def submit():
        con=sqlite3.connect('ticket.db')
        cur=con.cursor()
        tick=ticket_box
        cur.execute("INSERT INTO ticket VALUES (:calling_customer, :address, :telephone, :tech, :status, :model, :serial_number, :notes)",
                {
                'calling_customer':calling_customer.get(),
                'address':address.get(),
                'telephone':telephone.get(), 
                'tech':tech.get(), 
                'status':status.get(), 
                'model':model.get(), 
                'serial_number':serial_number.get(), 
                'notes':notes.get('1.0', END), 
                }

            )

        con.commit()
        con.close()

        calling_customer.delete(0,END)
        address.delete(0,END)
        telephone.delete(0,END)
        tech.delete(0,END)
        status.delete(0,END)
        model.delete(0,END)
        serial_number.delete(0,END)
        notes.delete(1.0,END)

        new.destroy()


    calling_customer=Entry(new, width=35,bg="white",borderwidth=1)
    calling_customer.grid(row=1,column=1, columnspan=3, padx=10, pady=10)
    address=Entry(new, width=35,bg="white",borderwidth=1)
    address.grid(row=2,column=1, columnspan=3, padx=10, pady=10)
    telephone=Entry(new, width=35, bg="white", borderwidth=1)
    telephone.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
    tech=Entry(new, width=35,bg="white",borderwidth=1)
    tech.grid(row=4,column=1, columnspan=3, padx=10, pady=10)
    status=Entry(new, width=35,bg="white",borderwidth=1)
    status.grid(row=5,column=1, columnspan=3, padx=10, pady=10)
    model=Entry(new, width=35,bg="white",borderwidth=1)
    model.grid(row=6,column=1, columnspan=3, padx=10, pady=10)
    serial_number=Entry(new, width=35,bg="white",borderwidth=1)
    serial_number.grid(row=7,column=1, columnspan=3, padx=10, pady=10)

    notes=Text(new, width=26, height=5, bg="white",borderwidth=1)
    notes.grid(row=8,column=1, columnspan=3, padx=10, pady=10)

    calling_customer_label=Label(new, text="Calling Company")
    calling_customer_label.grid(row=1, column=0, padx=10, pady=10)
    address_label=Label(new, text="Calling Company Address")
    address_label.grid(row=2, column=0, padx=10, pady=10)
    telephone_label=Label(new, text="Calling Company Telephone Number")
    telephone_label.grid(row=3, column=0, padx=10, pady=10)
    tech_label=Label(new, text="Last Tech Associated with Ticket")
    tech_label.grid(row=4, column=0, padx=10, pady=10)
    status_label=Label(new, text="Case Status")
    status_label.grid(row=5, column=0, padx=10, pady=10)        
    model_label=Label(new, text="Machine Model")
    model_label.grid(row=6, column=0, padx=10, pady=10)
    serial_number_label=Label(new, text="Machine Serial Number")
    serial_number_label.grid(row=7, column=0, padx=10, pady=10)
    notes_label=Label(new, text="Case Discription")
    notes_label.grid(row=8, column=0, padx=10, pady=10)

    submit_btn=Button(new, text="Submit Ticket", bg="lightgreen", command=submit)
    submit_btn.grid(row=9, column=3)

    con.commit()
    con.close()

def query():
	con=sqlite3.connect('ticket.db')
	cur=con.cursor()
	cur.execute("SELECT *, oid FROM ticket")
	records = cur.fetchall()
	print_records = '' #set variable equal to nothing. 
	for record in records:
		print_records += (str(record[0]) + ", " + str(record[1]) + ", " + " \t" + str(record[8]) + "\n")

	query_label = Label(root, text = print_records)
	query_label.grid(row=3, ipadx=1, column=0, columnspan=3, sticky=NW)

	con.commit()
	con.close()

def delete():
	con=sqlite3.connect('ticket.db')
	cur=con.cursor()
	#delete_record_number=delete_box.get()
	cur.execute("DELETE from ticket WHERE oid="+ ticket_box.get())
#execute the query code agian.
	cur.execute("SELECT *, oid FROM ticket")
	records = cur.fetchall()
	print_records = '' #set variable equal to nothing. 
	for record in records:
		print_records += (str(record[0]) + ", " + str(record[1]) + ", " + " \t" + str(record[8]) + "\n")

	query_label = Label(root, text = print_records)
	query_label.grid(row=3, ipadx=1, column=0, columnspan=3, sticky=NW)

	con.commit()
	con.close()

def pull():
	pull=Tk() 
	pull.title("Pull Record")
	pull.geometry("600x700")
	con=sqlite3.connect('ticket.db')
	cur=con.cursor()

	con.commit()
	con.close()

current_call_window=Label(root, text="Current Call Window", bg="white", fg="black", font="arial", height=2, width=20)
current_call_window.grid(row=0,column=0,padx=10, pady=1)

ticket_frame=LabelFrame(root, text="Ticket Number")
ticket_frame.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

ticket_box=Entry(ticket_frame, width=20, bg="white", borderwidth=1)
ticket_box.grid(row=0, column=0)

#Buttons
new_ticket_btn=Button(root, text="New Ticket", width=30, command=new)
new_ticket_btn.grid(row=1, column=0)

query_btn = Button(root, text="Show Records", width=30, command=query) 
query_btn.grid(row=2, column=0)
#Shows a list of all records created for the last year. 


delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=2, column=3)

pull_btn = Button(root, text="Pull Ticket", command=pull)
pull_btn.grid(row=0, column=3)

con.commit()
con.close()
root.mainloop() 
