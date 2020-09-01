from tkinter import *

rootwindow = Tk() 
#don't forget to loop the file with Tkinter
rootwindow.title("Ticket Please")
rootwindow.geometry("480x500")

#	LEGEND
#cc= Calling Company
#cca= Calling Compnay address
#cctel= calling compnay telephone number
#te= last tech dealing with ticket
#cde= case discription
#stats= case status
#mm= machine model
#msn=machine serial number

#	BUTTONS
sqlsend=Button(rootwindow, text="Save Ticket", bg="lightgreen")
sqlsend.grid(row=0, column=3)

#	LABELS
ticket=LabelFrame(rootwindow,text="Ticket #")
ticket.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
tickettxtbox=Entry(ticket, width=20, bg="white", borderwidth=1)
tickettxtbox.grid()

ccw=Label(text="Current Call Window", bg="white", fg="black", font="arial", height=2, width=20)
cclabel=Label(text="Calling Company")
ccalabel=Label(text="Calling Company Address")
cctellabel=Label(text="Calling Company Telephone Number")
telabel=Label(text="Last Tech Associated with Ticket")
statslabel=Label(text="Case Status")
mmlabel=Label(text="Machine Model")
msnlabel=Label(text="Machine Serial Number")

cdelabel=Label(text="Case Discription")

#	ENTRY
cc=Entry(rootwindow, width=35,bg="white",borderwidth=1)
cca=Entry(rootwindow, width=35,bg="white",borderwidth=1)
cctel=Entry(width=35, bg="white", borderwidth=1)
te=Entry(rootwindow, width=35,bg="white",borderwidth=1)
stats=Entry(rootwindow, width=35,bg="white",borderwidth=1)
mm=Entry(rootwindow, width=35,bg="white",borderwidth=1)
msn=Entry(rootwindow, width=35,bg="white",borderwidth=1)

cde=Text(rootwindow, width=26, height=3,bg="white",borderwidth=1)

#define text entry locations. You can pack or organize a widget.
#	ENTRY GRID

cc.grid(row=1,column=1, columnspan=3, padx=10, pady=10)
cca.grid(row=2,column=1, columnspan=3, padx=10, pady=10)
cctel.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
te.grid(row=4,column=1, columnspan=3, padx=10, pady=10)
stats.grid(row=5,column=1, columnspan=3, padx=10, pady=10)
mm.grid(row=6,column=1, columnspan=3, padx=10, pady=10)
msn.grid(row=7,column=1, columnspan=3, padx=10, pady=10)

cde.grid(row=8,column=1, columnspan=3, padx=10, pady=10)

#	LABEL GRID
ccw.grid(row=0,column=0,padx=10, pady=10)
cclabel.grid(row=1, column=0, padx=10, pady=10)
ccalabel.grid(row=2, column=0, padx=10, pady=10)
cctellabel.grid(row=3, column=0, padx=10, pady=10)
telabel.grid(row=4, column=0, padx=10, pady=10)
statslabel.grid(row=5, column=0, padx=10, pady=10)        
mmlabel.grid(row=6, column=0, padx=10, pady=10)
msnlabel.grid(row=7, column=0, padx=10, pady=10)

cdelabel.grid(row=8, column=0, padx=10, pady=10)


rootwindow.mainloop() 
