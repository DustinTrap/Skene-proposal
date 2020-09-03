from tkinter import *
import sqlite3

root=Tk() 
#don't forget to loop the file with Tkinter
root.title("Ticket Please")
root.geometry("500x500")

#Databases

#Create a databese or connect to one
conn = sqlite3.connect('ticketplease.db')
#Create a cursor that fetches and place
c = conn.cursor()
#create Table
c.execute("""CREATE TABLE IF NOT EXISTS ticketplease ( 
	tickettxtbox text, 
	cc text, 
	cca text, 
	cctel text, 
	te text, 
	stats text, 
	mm text, 
	msn text, 
	cde text 
	)""")

# Insert into Table
c.execute("INSERT INTO ticketplease VALUES (:tickettxtbox, :cc, :cca, :cctel, :te, :stats, :mm, :msn, :cde)",{
			'tickettxtbox':tickettxtbox.get(),
			'cc':cc.get(), 
			'cca':cca.get(),
			'cctel':cctel.get(),
			'te':te.get(),
			'state':stats.get(),
			'mm':mm.get(),
			'msn':msn.get(),
			'cde':cde.get()})


#	LEGEND
#cc= Calling Company
#cca= Calling Compnay address
#cctel= calling compnay telephone number
#te= last tech dealing with ticket
#cde= case discription
#stats= case status
#mm= machine model
#msn=machine serial number

#add drop down menu for new ticket or existing ticket

# Define "submit" command. 
def submit():
	cc.delete(0,END)
	cca.delete(0,END)
	cctel.delete(0,END)
	te.delete(0,END)
	stats.delete(0,END)
	mm.delete(0,END)
	msn.delete(0,END)
	cde.delete(1.0,END)


#	BUTTONS. For this button the command is "submit", 
#but submit as a command must be defined(def) first, so above
sqlsend=Button(text="Save Ticket", bg="lightgreen", command=submit)
sqlsend.grid(row=0, column=3)

ccw=Label(text="Current Call Window", bg="white", fg="black", font="arial", height=2, width=20)
ccw.grid(row=0,column=0,padx=10, pady=10)

ticket=LabelFrame(text="Ticket #")
ticket.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
tickettxtbox=Entry(ticket, width=20, bg="white", borderwidth=1)
tickettxtbox.grid()

cclabel=Label(text="Calling Company")
cclabel.grid(row=1, column=0, padx=10, pady=10)
cc=Entry(width=35,bg="white",borderwidth=1)
cc.grid(row=1,column=1, columnspan=3, padx=10, pady=10)


ccalabel=Label(text="Calling Company Address")
ccalabel.grid(row=2, column=0, padx=10, pady=10)
cca=Entry(width=35,bg="white",borderwidth=1)
cca.grid(row=2,column=1, columnspan=3, padx=10, pady=10)


cctellabel=Label(text="Calling Company Telephone Number")
cctellabel.grid(row=3, column=0, padx=10, pady=10)
cctel=Entry(width=35, bg="white", borderwidth=1)
cctel.grid(row=3, column=1, columnspan=3, padx=10, pady=10)


telabel=Label(text="Last Tech Associated with Ticket")
telabel.grid(row=4, column=0, padx=10, pady=10)
te=Entry(width=35,bg="white",borderwidth=1)
te.grid(row=4,column=1, columnspan=3, padx=10, pady=10)


statslabel=Label(text="Case Status")
statslabel.grid(row=5, column=0, padx=10, pady=10)        
stats=Entry(width=35,bg="white",borderwidth=1)
stats.grid(row=5,column=1, columnspan=3, padx=10, pady=10)


mmlabel=Label(text="Machine Model")
mmlabel.grid(row=6, column=0, padx=10, pady=10)
mm=Entry(width=35,bg="white",borderwidth=1)
mm.grid(row=6,column=1, columnspan=3, padx=10, pady=10)


msnlabel=Label(text="Machine Serial Number")
msnlabel.grid(row=7, column=0, padx=10, pady=10)
msn=Entry(width=35,bg="white",borderwidth=1)
msn.grid(row=7,column=1, columnspan=3, padx=10, pady=10)


cdelabel=Label(text="Case Discription")
cdelabel.grid(row=8, column=0, padx=10, pady=10)
cde=Text(width=26, height=5, bg="white",borderwidth=1)
cde.grid(row=8,column=1, columnspan=3, padx=10, pady=10)



#commit changes
conn.commit()
#close connection
conn.close()

root.mainloop() 
