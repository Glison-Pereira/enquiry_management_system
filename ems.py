from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def mtov():
	mw.withdraw()
	vw.deiconify()
	view()
def vtom():
	vw.withdraw()
	mw.deiconify()
	vw_addresse.delete(1.0,END)
def mtod():
	names=namee.get()
	res=log(names)
	if res==None:
		mw.withdraw()
		lg.deiconify()
	else:
		mw.withdraw()
		dw.deiconify()

def dtom():
	dw.withdraw()
	mw.deiconify()

def log(naam):
	con=None
	try:
		con=connect("database_name1.db")
		cursor=con.cursor()
		sql="select name from table_name1 where name='%s'"
		cursor.execute(sql%(naam))
		data=cursor.fetchone()
		return data
	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()

def save():
	nam=namee.get()
	phon=phonee.get()
	address=addresse.get(1.0,END)
	if nam.strip()=="" or phon.strip()=="" or address.strip()=="":
		showinfo("Mistake","Don't leave blank spaces")
		namee.delete(0,END)
		phonee.delete(0,END)
		addresse.delete(1.0,END)
		namee.focus()
		phonee.focus()
		addresse.focus()
	elif len(nam.strip())>30 or len(address.strip())>200:
		showinfo("Mistake","You can't enter so big name or big address")
		namee.delete(0,END)
		addresse.delete(1.0,END)
		namee.focus()
		addresse.focus()
	elif not(phon.isdigit()) or not(nam.strip().isalpha()):
		showinfo("Mistake","Your phone number should have digits and name should have alphabets only")
		namee.delete(0,END)
		phonee.delete(0,END)
		namee.focus()
		phonee.focus()
	elif len(phon.strip())>10 or len(phon.strip())<10:
		showinfo("Mistake","Phone number entered wrong")
		phonee.delete(0,END)
		phonee.focus()	
	elif int(phon)<1:
		showinfo("Mistake","Phone number entered wrong")
		phonee.delete(0,END)
		phonee.focus()
	else:
		res=log(nam)
		if res==None:
			mw.withdraw()
			lg.deiconify()
		else:
			con=None
			try:
				con=connect("database_name2.db")
				cursor=con.cursor()
				sql="insert into table_name2 values('%s','%s','%s','%s')"
				ptop=""
				if to.get()!=1 and on.get()!=1 and ch.get()!=1 and co.get()!=1:
					showinfo("Mistake","Atleast select some option")
				else:
					if to.get()==1:
						ptop+=" Requests for information about products or services offered. "
					if on.get()==1:
						ptop+=" Queries about the status of placed orders. "
					if ch.get()==1:
						ptop+=" Assistance with troubleshooting technical issues. "
					if co.get()==1:
						ptop+=" Inquiries regarding warranty coverage. "
					cursor.execute(sql % (nam,phon,address,ptop))
					showinfo("Success","Record Created")
					con.commit()  
					phonee.delete(0,END)
					addresse.delete(1.0,END)
					phonee.focus()
					addresse.focus() 
			except Exception as e:
				showerror("Error",e)
				con.rollback() 
			finally:
				if con is not None:
					con.close()

def logouts():
	con=None
	try:
		con=connect("database_name1.db")
		cursor=con.cursor()
		sql="delete from table_name1 where name='%s'"
		namest=namee.get()
		cursor.execute(sql % (namest))
		if cursor.rowcount==1:
			con.commit()   
	except Exception as e:
		showerror("Error",e)
		con.rollback() 
	finally:
		if con is not None:
			con.close()

def view():
	con=None
	try:
		con=connect("database_name2.db")
		cursor=con.cursor()
		sql="select * from table_name2"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			vw_addresse.insert(END,str(d)+'\n')
	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()

def delete():
	pho=dw_phonee.get()
	if pho.strip()=="":
		showinfo("Mistake","Don't leave blank spaces")
		dw_phonee.delete(0,END)
		dw_phonee.focus()
	elif len(pho.strip())>10 or len(pho.strip())<10:
		showinfo("Mistake","Phone number entered wrong")
		dw_phonee.delete(0,END)
		dw_phonee.focus()	
	elif not(pho.isdigit()):
		showinfo("Mistake","Your phone number should have digits only")
		dw_phonee.delete(0,END)
		dw_phonee.focus()
	elif int(pho)<1:
		showinfo("Mistake","Phone number entered wrong")
		dw_phonee.delete(0,END)
		dw_phonee.focus()
	else:
		con=None
		try:
			con=connect("database_name2.db")
			cursor=con.cursor()
			sql="delete from table_name2 where phone='%s' and query='%s' "
			pto=""
			if toe.get()!=1 and one.get()!=1 and che.get()!=1 and coe.get()!=1:
				showinfo("Mistake","Atleast select some option")
			else:
				if toe.get()==1:
					pto+=" Requests for information about products or services offered. "
				if one.get()==1:
					pto+=" Queries about the status of placed orders. "
				if che.get()==1:
					pto+=" Assistance with troubleshooting technical issues. "
				if coe.get()==1:
					pto+=" Inquiries regarding warranty coverage. "
				cursor.execute(sql % (pho,pto))
				if cursor.rowcount==1:
					con.commit()  
					showinfo("Success","record deleted") 
				else:
					showinfo("Success","record does not exist")
				dw_phonee.delete(0,END)
				dw_phonee.focus()
		except Exception as e:
			showerror("Error",e)
			con.rollback() 
		finally:
			if con is not None:
				con.close()


def table_name1():
	name=lg_namee.get()
	phone=lg_phonee.get()
	password=lg_passworde.get()
	if name.strip()=="" or phone.strip()=="" or password.strip()=="":
		showinfo("Mistake","Don't leave blank spaces")
		lg_namee.delete(0,END)
		lg_phonee.delete(0,END)
		lg_passworde.delete(0,END)
		lg_namee.focus()
		lg_phonee.focus()
		lg_passworde.focus()
	elif len(name.strip())>30 or len(password.strip())>10:
		showinfo("Mistake","You can't enter so big name or big password")
		lg_namee.delete(0,END)
		lg_passworde.delete(0,END)
		lg_namee.focus()
		lg_passworde.focus()
	elif not(phone.isdigit()) or not(name.strip().isalpha()):
		showinfo("Mistake","Your phone number should have digits and name should have alphabets only")
		lg_namee.delete(0,END)
		lg_phonee.delete(0,END)
		lg_namee.focus()
		lg_phonee.focus()
	elif len(phone.strip())>10 or len(phone.strip())<10:
		showinfo("Mistake","Phone number entered wrong")
		lg_phonee.delete(0,END)
		lg_phonee.focus()	
	elif int(phone)<1:
		showinfo("Mistake","Phone number entered wrong")
		lg_phonee.delete(0,END)
		lg_phonee.focus()
	else:
		con=None
		try:
			con=connect("database_name1.db")
			cursor=con.cursor()
			sql="insert into table_name1 values('%s','%s','%s')"
			cursor.execute(sql % (name,phone,password))
			con.commit()  
			lg_namee.delete(0,END)
			lg_phonee.delete(0,END)
			lg_passworde.delete(0,END)
			lg_namee.focus()
			lg_phonee.focus()
			lg_passworde.focus()
		except Exception as e:
			showerror("Error",e)
			con.rollback() 
		finally:
			if con is not None:
				con.close()
			lg.withdraw()
			mw.deiconify()


mw=Tk()
mw.title("table_name2 Management System")
mw.geometry("950x720+500+20")
mw.resizable(False,False)
mw.configure(bg="lightyellow")

f=("Times new Roman",25,"bold")

label=Label(mw,text="table_name2 Management System",font=f)
label.configure(bg="lightyellow",fg="red")
label.pack(pady=20)

to,on,co,ch=IntVar(),IntVar(),IntVar(),IntVar()
name=Label(mw,text="Enter your name: ",font=f)
namee=Entry(mw,font=f)
phone=Label(mw,text="Enter your phone number: ",font=f)
phonee=Entry(mw,font=f)
address=Label(mw,text="Enter your address: ",font=f)
addresse=ScrolledText(mw,height=5,width=20,font=f)
table_name2=Label(mw,text="Your Enquiries: ",font=f)
en1=Checkbutton(mw,text="Requests for information about products or services offered.",font=f,variable=to)
en2=Checkbutton(mw,text="Queries about the status of placed orders.",font=f,variable=on)
en3=Checkbutton(mw,text="Assistance with troubleshooting technical issues.",font=f,variable=co)
en4=Checkbutton(mw,text="Inquiries regarding warranty coverage.",font=f,variable=ch)
savee=Button(mw,text="Save",font=f,bg="darkred",fg="white",command=save)
viewe=Button(mw,text="View",font=f,bg="darkred",fg="white",command=mtov)
deletee=Button(mw,text="Delete",font=f,bg="darkred",fg="white",command=mtod)
logout=Button(mw,text="Logout",font=f,bg="darkred",fg="white",command=logouts)

name.configure(bg="lightyellow")
phone.configure(bg="lightyellow")
address.configure(bg="lightyellow")
table_name2.configure(bg="lightyellow")
en1.configure(bg="lightyellow")
en2.configure(bg="lightyellow")
en3.configure(bg="lightyellow")
en4.configure(bg="lightyellow")

name.place(x=20,y=80)
namee.place(x=290,y=80)
phone.place(x=20,y=140)
phonee.place(x=420,y=140)
address.place(x=20,y=200)
addresse.place(x=320,y=200)
table_name2.place(x=20,y=400)
en1.place(x=270,y=400)
en2.place(x=270,y=460)
en3.place(x=270,y=520)
en4.place(x=270,y=580)
savee.place(x=50,y=640)
viewe.place(x=350,y=640)
deletee.place(x=620,y=640)
logout.place(x=800,y=20)

lg=Toplevel(mw)
lg.title("table_name2 Management System")
lg.geometry("950x720+500+20")
lg.resizable(False,False)
lg.configure(bg="lightyellow")

lg_label=Label(lg,text="table_name1",font=f)
lg_label.configure(bg="lightyellow",fg="red")
lg_label.pack(pady=20)

lg_name=Label(lg,text="Enter your name: ",font=f)
lg_namee=Entry(lg,font=f)
lg_phone=Label(lg,text="Enter your phone number: ",font=f)
lg_phonee=Entry(lg,font=f)
lg_password=Label(lg,text="Enter your password: ",font=f)
lg_passworde=Entry(lg,font=f)
table_name1e=Button(lg,text="table_name1",font=f,bg="darkred",fg="white",command=table_name1)

lg_name.configure(bg="lightyellow")
lg_phone.configure(bg="lightyellow")
lg_password.configure(bg="lightyellow")

y=20
lg_name.pack(pady=y)
lg_namee.pack(pady=y)
lg_phone.pack(pady=y)
lg_phonee.pack(pady=y)
lg_password.pack(pady=y)
lg_passworde.pack(pady=y)
table_name1e.pack(pady=y)

vw=Toplevel(mw)
vw.title("table_name2 Management System")
vw.geometry("950x720+500+20")
vw.resizable(False,False)
vw.configure(bg="lightyellow")

vw_label=Label(vw,text="View",font=f)
vw_label.configure(bg="lightyellow",fg="red")
vw_label.pack(pady=20)

vw_addresse=ScrolledText(vw,height=10,width=40,font=f)
vw_backe=Button(vw,text="Back",font=f,bg="darkred",fg="white",command=vtom)

vw_addresse.pack(pady=y)
vw_backe.pack(pady=y)

dw=Toplevel(mw)
dw.title("table_name2 Management System")
dw.geometry("950x720+500+20")
dw.resizable(False,False)
dw.configure(bg="lightyellow")

dw_label=Label(dw,text="Delete",font=f)
dw_label.configure(bg="lightyellow",fg="red")
dw_label.pack(pady=20)

toe,one,coe,che=IntVar(),IntVar(),IntVar(),IntVar()
dw_phone=Label(dw,text="Enter your phone number: ",font=f)
dw_phonee=Entry(dw,font=f)
dw_table_name2=Label(dw,text="Your Enquiries: ",font=f)
dw_en1=Checkbutton(dw,text="Requests for information about products or services offered.",font=f,variable=toe)
dw_en2=Checkbutton(dw,text="Queries about the status of placed orders.",font=f,variable=one)
dw_en3=Checkbutton(dw,text="Assistance with troubleshooting technical issues.",font=f,variable=coe)
dw_en4=Checkbutton(dw,text="Inquiries regarding warranty coverage.",font=f,variable=che)
dw_backe=Button(dw,text="Back",font=f,bg="darkred",fg="white",command=dtom)
dw_delete=Button(dw,text="Delete",font=f,bg="darkred",fg="white",command=delete)

dw_phone.configure(bg="lightyellow")
dw_table_name2.configure(bg="lightyellow")
dw_en1.configure(bg="lightyellow")
dw_en2.configure(bg="lightyellow")
dw_en3.configure(bg="lightyellow")
dw_en4.configure(bg="lightyellow")

dw_phone.pack(pady=10)
dw_phonee.pack(pady=10)
dw_table_name2.pack(pady=10)
dw_en1.pack(pady=10)
dw_en2.pack(pady=10)
dw_en3.pack(pady=10)
dw_en4.pack(pady=10)
dw_backe.pack(pady=10)
dw_delete.pack(pady=10)


lg.withdraw()
vw.withdraw()
dw.withdraw()

mw.mainloop()
