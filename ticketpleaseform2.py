from tkinter import *
import sqlite3

root=Tk() 
#don't forget to loop the file with Tkinter
root.title("Ticket Please")
root.geometry("600x700")

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
con=sqlite3.connect('ticketplease.db')
#Create a cursor that fetches and places
cur=con.cursor()

#Databases

#create Table 
cur.execute("""CREATE TABLE IF NOT EXISTS ticketplease ( 
	ticket_number null, 
	calling_customer null, 
	address null, 
	telephone null, 
	tech_assigned null, 
	status null, 
	model null, 
	serial_number null, 
	notes null 
	)""")


#submit function
def submit():
	con=sqlite3.connect('ticketplease.db')
	cur=con.cursor()
	tick=ticketbox
	cur.execute("INSERT INTO ticketplease VALUES (:ticketbox, :cc, :cca, :cctel, :te, :stats, :mm, :msn, :notes)",
			{
			'ticketbox':tick.get(),
			'cc':cc.get(),
			'cca':cca.get(),
			'cctel':cctel.get(), 
			'te':te.get(), 
			'stats':stats.get(), 
			'mm':mm.get(), 
			'msn':msn.get(), 
			'notes':notes.get('1.0', END), 
			}

		)

	con.commit()
	con.close()

	tick.delete(0, END)
	cc.delete(0,END)
	cca.delete(0,END)
	cctel.delete(0,END)
	te.delete(0,END)
	stats.delete(0,END)
	mm.delete(0,END)
	msn.delete(0,END)
	notes.delete(1.0,END)	 

def query():
	con=sqlite3.connect('ticketplease.db')
	cur=con.cursor()
	cur.execute("SELECT *, oid FROM ticketplease")
	records = cur.fetchall()
	print_records = '' #set variable equal to nothing. 
	for record in records:
		print_records += (str(record[0]) + ", " + str(record[1]) + ", " + " \t" + str(record[9]) + "\n")

	query_label = Label(root, text = print_records)
	query_label.grid(row=10, ipadx=1, column=1, columnspan=3, sticky=NE)

	con.commit()
	con.close()

#def delete():
#	con=sqlite3.connect('ticketplease.db')
#	cur=con.cursor()
#	#delete_record_number=delete_box.get()
#	cur.execute("DELETE from ticketplease WHERE oid="+ delete_box.get())
#execute the query code agian.
#	cur.execute("SELECT *, oid FROM ticketplease")
#	records = cur.fetchall()
#	print_records = '' #set variable equal to nothing. 
#	for record in records:
#		print_records += (str(record[0]) + ", " + str(record[1]) + ", " + " \t" + str(record[9]) + "\n")

#	query_label = Label(root, text = print_records)
#	query_label.grid(row=10, ipadx=1, column=1, columnspan=3, sticky=NE)

#	con.commit()
#	con.close()

def pull():
	pull=Tk() 
	pull.title("Pull Record")
	pull.geometry("600x700")
	con=sqlite3.connect('ticketplease.db')
	cur=con.cursor()

	con.commit()
	con.close()

delete_box = Entry(root, width=20, bg="white", borderwidth=1)
delete_box.grid(row=9, column=1, padx=10, pady=0)

ticket=LabelFrame(root, text="Ticket #")
ticket.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

ticketbox=Entry(ticket, width=20, bg="white", borderwidth=1)
ticketbox.grid(row=0, column=0)

cc=Entry(root, width=35,bg="white",borderwidth=1)
cc.grid(row=1,column=1, columnspan=3, padx=10, pady=10)
cca=Entry(root, width=35,bg="white",borderwidth=1)
cca.grid(row=2,column=1, columnspan=3, padx=10, pady=10)
cctel=Entry(root, width=35, bg="white", borderwidth=1)
cctel.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
te=Entry(root, width=35,bg="white",borderwidth=1)
te.grid(row=4,column=1, columnspan=3, padx=10, pady=10)
stats=Entry(root, width=35,bg="white",borderwidth=1)
stats.grid(row=5,column=1, columnspan=3, padx=10, pady=10)
mm=Entry(root, width=35,bg="white",borderwidth=1)
mm.grid(row=6,column=1, columnspan=3, padx=10, pady=10)
msn=Entry(root, width=35,bg="white",borderwidth=1)
msn.grid(row=7,column=1, columnspan=3, padx=10, pady=10)

notes=Text(root, width=26, height=5, bg="white",borderwidth=1)
notes.grid(row=8,column=1, columnspan=3, padx=10, pady=10)

ccw=Label(root, text="Current Call Window", bg="white", fg="black", font="arial", height=2, width=20)
ccw.grid(row=0,column=0,padx=10, pady=10)

cclabel=Label(root, text="Calling Company")
cclabel.grid(row=1, column=0, padx=10, pady=10)
ccalabel=Label(root, text="Calling Company Address")
ccalabel.grid(row=2, column=0, padx=10, pady=10)
cctellabel=Label(root, text="Calling Company Telephone Number")
cctellabel.grid(row=3, column=0, padx=10, pady=10)
telabel=Label(root, text="Last Tech Associated with Ticket")
telabel.grid(row=4, column=0, padx=10, pady=10)
statslabel=Label(root, text="Case Status")
statslabel.grid(row=5, column=0, padx=10, pady=10)        
mmlabel=Label(root, text="Machine Model")
mmlabel.grid(row=6, column=0, padx=10, pady=10)
msnlabel=Label(root, text="Machine Serial Number")
msnlabel.grid(row=7, column=0, padx=10, pady=10)
noteslabel=Label(root, text="Case Discription")
noteslabel.grid(row=8, column=0, padx=10, pady=10)

#Buttons
submit_btn=Button(root, text="Save Ticket", bg="lightgreen", command=submit)
submit_btn.grid(row=0, column=3, pady=(0,15))

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=0, column=3, pady=(40,0))

#delete_btn = Button(root, text="Delete Record", command=delete)
#delete_btn.grid(row=9, column=4, sticky=N)

pull_btn = Button(root, text="Pull Ticket", command=pull)
pull_btn.grid(row=9, column=0, sticky=N)

con.commit()
con.close()
root.mainloop() 
