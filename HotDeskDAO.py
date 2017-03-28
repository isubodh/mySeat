#!/usr/hin/python
import sqlite3

##Run when ever the user want to add a desk
## Ensures that exits a table for making entry

def CreateDesk():
	conn = sqlite3.connect('HotDesk.sqlite')
	cursor = conn.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS HotDesk (
	Floor INTEGER,
	DeskNo INTEGER,
	Free_date DATE,
	Remark TEXT,
	Primary Key(DeskNo, Free_date)
	);''')
	
	cursor.close()
	conn.commit()
	
## Find all desk free onall days
def findAllDesk():
	CreateDesk()
	conn = sqlite3.connect('HotDesk.sqlite')
	cursor = conn.cursor()
	
	FreeDesk = list()
	FreeDeskRS = cursor.execute('''SELECT rowid, Floor,
				DeskNo, Free_date, Remark from  HotDesk 
				order by Free_date asc''')
	for row in FreeDeskRS:
		FreeDesk.append({'rowid' : row[0], 'floor' : row[1], 'deskno' : row[2], 'free_date' : row[3], 'remark' : row[4]})
	
	cursor.close()
	conn.commit()
	return FreeDesk

## Find all desk free on a given day
def findDeskOnDate(onDate):
	CreateDesk()
	conn = sqlite3.connect('HotDesk.sqlite')
	cursor = conn.cursor()	
	FreeDesk = list()
	FreeDeskRS = cursor.execute('''SELECT rowid, Floor,
				DeskNo, Free_date, Remark from  HotDesk
				where Free_date = (?)
				order by Free_date asc''',(onDate,))
	for row in FreeDeskRS:
		FreeDesk.append({'rowid' : row[0], 'floor' : row[1], 'deskno' : row[2], 'free_date' : row[3], 'remark' : row[4]})
	
	cursor.close()
	conn.commit()
	return FreeDesk				

def CreateUser():
	conn = sqlite3.connect('HotDesk.sqlite')
	cursor = conn.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS User (
	user_name, user_email UNIQUE, user_password
	);''')
	cursor.close()
	conn.commit()

def AddDesk(atFloor, Desk, onDate, Rem):
	conn = sqlite3.connect('HotDesk.sqlite')
	cursor = conn.cursor()
	cursor.execute('''
	INSERT OR IGNORE INTO HotDesk (Floor, DeskNo, Free_date, Remark)
	VALUES (?,?,?,?);''',(atFloor, Desk, onDate, Rem))
	cursor.close()
	conn.commit()
	

def allocatedDesk():
	allocateDesk = list()
	conn = sqlite3.connect('HotDesk.sqlite')
	cursor = conn.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS bookedHotDesk (
	Floor INTEGER,
	DeskNo  INTEGER,
	Free_date DATE,
	Remark TEXT,
	Primary Key(DeskNo, Free_date)
	);''')
	
	allocateDeskRS = cursor.execute('''
	SELECT rowid, Floor, DeskNo, Free_date, Remark
	from bookedHotDesk order by Free_date asc''')
	
	for row in allocateDeskRS:
		allocateDesk.append({'rowid' : row[0], 'floor' : row[1], 'deskno' : row[2], 'free_date' : row[3], 'remark' : row[4]})
		
	return allocateDesk

# Book a desk
def bookDesk(index):
	print("Request with : ", index)
	bookedDesk = list()
	if not index:
		return bookedDesk
	conn = sqlite3.connect('HotDesk.sqlite')
	cursor = conn.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS bookedHotDesk (
	Floor INTEGER,
	DeskNo  INTEGER,
	Free_date DATE,
	Remark TEXT,
	Primary Key(DeskNo, Free_date)
	);''')

	bookedDeskRS = cursor.execute('''
	SELECT rowid, Floor, DeskNo, Free_date, Remark
	from HotDesk where rowid = (?)''', (index,))	
	
	for row in bookedDeskRS:
		bookedDesk.append({'rowid' : row[0], 'floor' : row[1], 'deskno' : row[2], 'free_date' : row[3], 'remark' : row[4]})
		
	if not bookedDesk:
		return bookedDesk
	
	# Add to booked table
	cursor.execute('''
	INSERT OR IGNORE INTO bookedHotDesk (
	Floor, DeskNo, Free_date, Remark) 
	VALUES (?,?,?,?)''',(bookedDesk[0]['floor'],bookedDesk[0]['deskno'],bookedDesk[0]['free_date'],bookedDesk[0]['remark']))
	
	# Delte form HotDesk
	cursor.execute('''DELETE from HotDesk where rowid = (?)''',(index,))
	
	cursor.execute
	conn.commit()
	return bookedDesk
	
if __name__ == "__main__":
	import datetime
	CreateDesk()
	tdstr = str(datetime.date.today())
	Today = tdstr[8:] + '/' + tdstr[5:7] + '/' + tdstr[:4]
	Desk = findDeskOnDate(Today)
	for row in Desk:
		print(row)
	
	AddDesk(5, 357, '25/07/2017', 'Subodh Desk')
	AddDesk(5, 357, '26/07/2017', 'Subodh Desk')
	AddDesk(5, 357, '27/07/2017', 'Subodh Desk')
	AddDesk(5, 357, '28/07/2017', 'Subodh Desk')
	AddDesk(5, 357, '29/07/2017', 'Subodh Desk')
	
	Desk = findAllDesk()
	print('Desk Free Obj ', type(Desk))
	for row in Desk:
		print(row)