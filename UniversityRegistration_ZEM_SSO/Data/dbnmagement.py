import sqlite3
from tkinter import messagebox

class dbmange:
    def __init__(self,address):
        self.conn = sqlite3.connect(address)
        self.cur = self.conn.cursor()

    def create(self):
        # self.cur.execute('alter TABLE COURSES drop column "CRS_TCH_ID" ')
        # self.cur.execute('alter TABLE COURSES drop column "CRS_TCH_ID" INT')
        # self.cur.execute('drop TABLE Student')
        # self.cur.execute('drop TABLE Teacher')
        # self.cur.execute('drop TABLE Course')
        # self.cur.execute('drop TABLE Mark')
        try:
            # self.cur.execute('CREATE TABLE Student (SID INT PRIMARY KEY ,FSNAME NVARCHAR(50),LSNAME NVARCHAR(50))')
            # self.cur.execute('CREATE TABLE Teacher (TID INT PRIMARY KEY ,FTNAME NVARCHAR(50),LTNAME NVARCHAR(50))')
            # self.cur.execute('CREATE TABLE Course (CID INT PRIMARY KEY ,CNAME NVARCHAR(50),CUNIT INT,CTID INT)')
            # self.cur.execute('CREATE TABLE Mark (MID INT PRIMARY KEY ,SID INT,TID INT,CID INT,MARK INT)')

            self.cur.execute(
                'CREATE TABLE "STUDENTS"         ("STD_ID" INTEGER NOT NULL,"STD_FNAME" TEXT,"STD_LNAME" TEXT,PRIMARY KEY("STD_ID"))')
            self.cur.execute(
                'CREATE TABLE "TEACHERS"         ("TCH_ID" INTEGER NOT NULL, "TCH_FNAME" TEXT NOT NULL, "TCH_LNAME" TEXT, PRIMARY KEY("TCH_ID"))')
            self.cur.execute(
                'CREATE TABLE "COURSES"          ("CRS_ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,"CRS_NAME"	TEXT NOT NULL UNIQUE,"CRS_UNIT_COUNT"	INTEGER NOT NULL DEFAULT 1)')
            self.cur.execute(
                'CREATE TABLE "COURSES_TEACHERS" ("CRS_ID"	INTEGER NOT NULL,"TCH_ID"	INTEGER NOT NULL,PRIMARY KEY("CRS_ID","TCH_ID"))')
            self.cur.execute(
                'CREATE TABLE "STUDENT_COURSES_TEACHERS" ("STD_ID"	INTEGER NOT NULL,"CRS_ID"	INTEGER NOT NULL,"TCH_ID"	INTEGER NOT NULL,PRIMARY KEY("STD_ID","CRS_ID","TCH_ID"))')
            self.cur.execute(
                'CREATE TABLE "MARKS" (	"MRK_STD_ID"	INTEGER NOT NULL,	"MRK_SEMESTER"	TEXT NOT NULL,	"MRK_NO"	INTEGER NOT NULL,	"MRK_CRS_ID"	INTEGER,	"MRK_TCH_ID"	INTEGER)')

            self.conn.commit()
        except Exception as e:
            e = str(e)
            # if ('already exists' in e):
            print(e)

    # def deletebaskets(self):
    #    self.cur.execute('Delete from BasketProd')
    #    self.conn.commit()

    def insert(self,query,params):
        try:
            self.cur.execute(query,params )
            self.conn.commit()
            # messagebox.showinfo('Alert', 'ثبت اطلاعات با موفقیت انجام شد.')
            return 'True'
        except Exception as e:
            # messagebox.showinfo('Alert', 'در ثبت اطلاعات خطایی رخ داده است. (' + str(e) + '(')
            return str(e)

    def select(self,query):
        try:
            self.cur.execute(query)
            L = self.cur.fetchall()
            return L
        except Exception as e:
            messagebox.showinfo('Alert', 'در بازیابی اطلاعات خطایی رخ داده است. (' + str(e) + '(')

    def delete(self,q):
        try:
            self.cur.execute(q)
            self.conn.commit()
            messagebox.showinfo('Alert', 'حذف اطلاعات با موفقیت انجام شد.')
        except Exception as e:
            messagebox.showinfo('Alert', 'در حذف اطلاعات خطایی رخ داده است. (' + str(e) + '(')

    def update(self,q):
        try:
            self.cur.execute(q)
            self.conn.commit()
            messagebox.showinfo('Alert', 'بهنگام سازی اطلاعات با موفقیت انجام شد.')
        except Exception as e:
            messagebox.showinfo('Alert', 'در بهنگام سازی اطلاعات خطایی رخ داده است. (' + str(e) + '(')