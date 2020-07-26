import logging
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import bs4
import requests
import socket

logging.basicConfig(filename='example.log',level=logging.INFO)

root = Tk()
root.title("s.m.s")
root.geometry("600x550+500+100")

def f1():
	root.withdraw()        #main to add 
	addst.deiconify()		
def f2():
	addst.withdraw()       #add to main        add to main
	root.deiconify()
def f5():
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/abc123")              #addsave
        rno = int(entRno.get())
        name = entName.get()
        marks = int(entMarks.get())
        if(rno <= 0):
            messagebox.showerror(title = "Error", message = "Rno -> Positive Integers Only")
            entRno.focus()
            entRno.delete(0 , END)
        elif(len(name) < 2):
            messagebox.showerror(title = "Error", message = "Enter valid Name")
            entName.focus()
            entName.delete(0 , END)
        elif(marks < 0 or marks > 100):
            messagebox.showerror(title = "Error", message = "Marks -> 1 to 100 only")
            entMarks.focus()
            entMarks.delete(0 , END)
        else:
            cursor = con.cursor()
            sql = "insert into project values('%d' , '%s' , '%d')"
            args = (rno , name , marks)
            cursor.execute(sql % args)
            con.commit()
            msg = str(cursor.rowcount) + " record inserted "
            messagebox.showinfo("Status " , msg)
            logging.info('Added Rno : %d , Name : %s , Marks : %d', rno,name,marks)
            entRno.delete(0 , END)
            entName.delete(0 , END)
            entMarks.delete(0 , END)
            entRno.focus()
            
    except ValueError:
        if(entRno.get()==""):
            messagebox.showerror(title = "Error", message = "Rno cannot be empty")
            entRno.focus()
            entRno.delete(0 , END)
        elif(entRno.get().isalpha()):
            messagebox.showerror(title = "Error", message = "Rno ->Positive Integers Only")
            entRno.focus()
            entRno.delete(0 , END)
        elif(entName.get()==""):
            messagebox.showerror(title = "Error", message = "Name cannot be empty")
            entName.focus()
            entName.delete(0 , END)
        elif(entName.get().isdigit()):
            messagebox.showerror(title = "Error", message = "Name -> Characters Only")
            entName.focus()
            entName.delete(0 , END)
        elif(entMarks.get()==""):
            messagebox.showerror(title = "Error", message = "Marks cannot be empty")
            entMarks.focus()
            entMarks.delete(0 , END)
        elif(entMarks.get().isalpha()):
            messagebox.showerror(title = "Error", message = "Marks -> Positive Integers Only")
            entMarks.focus()
            entMarks.delete(0 , END)
        else:
            messagebox.showerror(title = "Error", message = "Enter proper values")
            entRno.focus()
    except cx_Oracle.DatabaseError as e: 
        messagebox.showerror("Databse Error" , "Rno Already Exists")
        con.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
def f3():
	root.withdraw()
	viewst.deiconify()                                                  #main to view
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from project"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "r: " + str(d[0]) + "\tn:  " + d[1] +  "\t\tm : " + str(d[2]) + "\n" 
		stData.insert(INSERT , msg)
	except cx_Oracle.DatabaseError as e: 
		messagebox.showerror("Wrong  " , e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f4():
    viewst.withdraw()              #view to main
    root.deiconify()
    stData.delete('1.0' , END)
def f6():
	root.withdraw()                                    #main to update
	updatest.deiconify()
    
def f11():
	updatest.withdraw()       #update to main        updateback to main
	root.deiconify()

def f7():
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/abc123")
        rno = int(entURno.get())
        name = entUName.get()			#updatesave                       #updatesave
        marks = int(entUMarks.get())
        if(rno <= 0):
            messagebox.showerror(title = "Error", message = "Rno -> Positive Integers Only")
            entURno.focus()
            entURno.delete(0 , END)
        
        elif(len(name) < 2):
            messagebox.showerror(title = "Error", message = "Enter valid Name")
            entUName.focus()
            entUName.delete(0 , END)
        elif(marks < 0 or marks > 100):
            messagebox.showerror(title = "Error", message = "Marks -> 1 to 100 only")
            entUMarks.focus()
            entUMarks.delete(0 , END)
        else:
            cursor = con.cursor()
            sql = "update project set name = '%s' , marks = '%d' where rno = '%d' "
            args = (name , marks , rno)
            cursor.execute(sql % args)
            con.commit()
            if(cursor.rowcount == 0):
                msg = str("Record doesn't exist ")
                #msg = str(cursor.rowcount) + " record updated "
                messagebox.showinfo("Status " , msg)
                entURno.delete(0 , END)
                entUName.delete(0 , END)
                entUMarks.delete(0 , END)
                entURno.focus()
            else:
                msg = str(cursor.rowcount) + " record updated "
                messagebox.showinfo("Status " , msg)
                logging.info('Updated Rno : %d , Name : %s , Marks : %d', rno,name,marks)
                entURno.delete(0 , END)
                entUName.delete(0 , END)
                entUMarks.delete(0 , END)
                entURno.focus()
    except ValueError:
        if(entURno.get()==""):
            messagebox.showerror(title = "Error", message = "Rno cannot be empty")
            entURno.focus()
            entURno.delete(0 , END)
        elif(entURno.get().isalpha()):
            messagebox.showerror(title = "Error", message = "Rno ->Positive Integers Only")
            entURno.focus()
            entURno.delete(0 , END)
        elif(entUName.get()==""):
            messagebox.showerror(title = "Error", message = "Name cannot be empty")
            entUName.focus()
            entUName.delete(0 , END)
        elif(entUName.get().isdigit()):
            messagebox.showerror(title = "Error", message = "Name -> Characters Only")
            entUName.focus()
            entUName.delete(0 , END)
        elif(entMarks.get()==""):
            messagebox.showerror(title = "Error", message = "Marks cannot be empty")
            entUMarks.focus()
            entUMarks.delete(0 , END)
        elif(entUMarks.get().isalpha()):
            messagebox.showerror(title = "Error", message = "Marks -> Positive Integers Only")
            entUMarks.focus()
            entUMarks.delete(0 , END)
        else:
            messagebox.showerror(title = "Error", message = "Enter proper values")
    except cx_Oracle.DatabaseError as e: 
        messagebox.showerror("Wrong  " , e)
        con.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
            
def f10():
	root.withdraw()                                    #main to delete
	deletest.deiconify()
    
def f12():
	deletest.withdraw()       #delete to main       deleteback to main
	root.deiconify()
				
def f8():
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/abc123")
        rno = int(entDRno.get())
        if(rno <= 0):
            messagebox.showerror(title = "Error", message = "Rno ->Positive Integers Only")
            entDRno.delete(0 , END)
            entDRno.focus()
        else:
            cursor = con.cursor()
            #sql = "insert into project values ('%d' , '%s' , '%d')"
            sql = "delete from project where rno = %d "
            args = (rno)                                                                                  #deletesave
            cursor.execute(sql % args)
            con.commit()
            if(cursor.rowcount == 0):
                msg = str("Record doesn't exist ")
            else:
                msg = str(cursor.rowcount) + " record deleted "                     
                messagebox.showinfo("Status " , msg)
                entDRno.delete(0 , END)
                entDRno.focus()
    except ValueError:
        if(entDRno.get()==""):
            messagebox.showerror(title = "Error", message = "Rno cannot be empty")
            entRno.focus()
            entDRno.delete(0 , END)
        elif(entRno.get().isalpha()):
            messagebox.showerror(title = "Error", message = "Rno ->Positive Integers Only")
            entRno.focus()
            entRno.delete(0 , END)
        else:
            messagebox.showerror(title = "Error", message = "pata nai re")
    except cx_Oracle.DatabaseError as e: 
        messagebox.showerror("Wrong  " , e)
        con.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
            
def last(n):
    return n[0]
def sort(tuples):
    return sorted(tuples , key = last)

            
def f13():
    import cx_Oracle
    import matplotlib.pyplot as plt
    import numpy as np
    con = None
    cursor = None
    try:
        a1 , a2 , a3 = [] , [] , []
        list , final = [] , []
        con = cx_Oracle.connect("system/abc123")
        cursor = con.cursor()
        sql = "select marks , rno , name from project"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row!= None:
            list.append(row)
            row = cursor.fetchone()
        list = sort(list)
        l = len(a3)
        for i in range(0 , 5):
            y = list[l-1]
            final.append(y)
            l = l-1
        for i in final:
            a1.append(i[0])
            a2.append(i[1])
            a3.append(i[2])
        a = np.arange(len(a3))
        plt.bar(a , a1 , label="marks" , color = "b")
        plt.title("graph")
        plt.xlabel("Name of Student")
        plt.ylabel("MArks")
        plt.xticks(a , a3)
        plt.grid()
        plt.legend()
        plt.show()
    except IndexError:
        messagebox.showerror(title = "Error", message = "At least 5 entries expected")
    except cx_Oracle.DatabaseError as e: 
        messagebox.showerror("Wrong  " , e)
        con.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
	
btnAdd = Button(root , text = "Add " , font=("arial" , 18 , "bold") , width = 10 , command = f1)
btnView = Button(root , text = "View" , font=("arial" , 18 , "bold") , width = 10 , command = f3)
btnUpdate = Button(root , text = "Update" , font=("arial" , 18 , "bold") , width = 10 , command = f6)
btnDelete = Button(root , text = "Delete" , font=("arial" , 18 , "bold") , width = 10 , command = f10)
btnGraph = Button(root , text = "Graph" , font=("arial" , 18 , "bold") , width = 10 , command = f13 )
lblQuote = Label(root , text = "Quote Of The Day" , font = ("chiller" , 18 , "bold"))
lblDisplay = Label(root , text = "" , font = ("arial" , 10  , "italic"))
lblTemp = Label(root , text = "Temp" , font = ("chiller" , 18 , "bold") , width = 10)
lblTempDisplay = Label(root , text = "" , font = ("arial" , 10 , "italic"))

try:
    res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
    soup = bs4.BeautifulSoup(res.text , 'lxml')
    quote = soup.find('img' , {"class" : "p-qotd"})
    ans = quote['alt']

    #city = input("location : ")
    socket.create_connection(("www.google.com" , 80))
    a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
    a2 = "&q=" + "thane"	
    a3 = "&appid=c6e315d09197cec231495138183954bd"
    api_address = a1 + a2 + a3
    res1 = requests.get(api_address)
    data = res1.json()
    main = data['main']
    temp = main['temp']
except OSError:
	print("check internet connection")

btnAdd.pack(pady = 10)
btnView.pack(pady = 10)
btnUpdate.pack(pady = 10)
btnDelete.pack(pady = 10)
btnGraph.pack(pady = 10)
lblQuote.pack(pady = 10)
lblDisplay.config(text = ans)
lblDisplay.pack(pady = 10)
lblTemp.pack(pady = 10)
lblTempDisplay.config(text = temp)
lblTempDisplay.pack(pady = 10)

addst = Toplevel(root)
addst.title("Add Student ")
addst.geometry("600x500+500+100")
addst.withdraw()
lblRno = Label(addst , text = "enter rno " , font=("arial" , 18 , "bold"))
entRno = Entry(addst , bd = 5 , font=("arial" , 18 , "bold"))
lblName = Label(addst , text = "enter name " , font=("arial" , 18 , "bold"))
entName = Entry(addst , bd = 5 , font=("arial" , 18 , "bold"))
lblMarks = Label(addst , text = "enter marks" ,  font=("arial" , 18 , "bold"))
entMarks = Entry(addst , bd = 5 , font=("arial" , 18 , "bold"))
btnAddSave = Button(addst , text = "Save" , font=("arial" , 18 , "bold") , command = f5)
btnAddBack = Button(addst , text = "Back" , font=("arial" , 18 , "bold") , command = f2)

lblRno.pack(pady = 5)
entRno.pack(pady = 5)
lblName.pack(pady = 5)
entName.pack(pady = 5)
lblMarks.pack(pady = 5)
entMarks.pack(pady = 5)
btnAddSave.pack(pady = 5)
btnAddBack.pack(pady = 5)

viewst = Toplevel(root)
viewst.title("View Student")
viewst.geometry("600x500+500+100")
viewst.withdraw()

stData = scrolledtext.ScrolledText(viewst , width = 40 , height = 10)
btnViewBack = Button(viewst , text = "Back" , font=("arial" , 18 , "bold") , command = f4)

stData.pack()
btnViewBack.pack()

updatest = Toplevel(root)
updatest.title("Update Student ")
updatest.geometry("600x500+500+100")
updatest.withdraw()
lblURno = Label(updatest , text = "enter rno " , font=("arial" , 18 , "bold"))
entURno = Entry(updatest , bd = 5 , font=("arial" , 18 , "bold"))
lblUName = Label(updatest , text = "enter name " , font=("arial" , 18 , "bold"))
entUName = Entry(updatest , bd = 5 , font=("arial" , 18 , "bold"))
lblUMarks = Label(updatest , text = "enter marks" ,  font=("arial" , 18 , "bold"))
entUMarks = Entry(updatest , bd = 5 , font=("arial" , 18 , "bold"))
btnUpdateSave = Button(updatest , text = "Save" , font=("arial" , 18 , "bold") , command = f7)
btnUpdateBack = Button(updatest , text = "Back" , font=("arial" , 18 , "bold") , command = f11)

lblURno.pack(pady = 5)
entURno.pack(pady = 5)
lblUName.pack(pady = 5)
entUName.pack(pady = 5)
lblUMarks.pack(pady = 5)
entUMarks.pack(pady = 5)
btnUpdateSave.pack(pady = 5)
btnUpdateBack.pack(pady = 5)


deletest = Toplevel(root)
deletest.title("Delete Student ")
deletest.geometry("600x500+500+100")
deletest.withdraw()
lblDRno = Label(deletest , text = "enter rno " , font=("arial" , 18 , "bold"))
entDRno = Entry(deletest , bd = 5 , font=("arial" , 18 , "bold"))
btnDeleteSave = Button(deletest , text = "Delete" , font=("arial" , 18 , "bold") , command = f8)
btnDeleteBack = Button(deletest , text = "Back" , font=("arial" , 18 , "bold") , command = f12)

lblDRno.pack(pady = 5)
entDRno.pack(pady = 5)
btnDeleteSave.pack(pady = 5)
btnDeleteBack.pack(pady = 5)

root.mainloop()
